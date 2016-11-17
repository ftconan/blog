$(function(){

});

//各级栏目之间联动
$("body").on("change","#classificationIdLevel",function(){
    linkage($("#classificationIdLevel").val());
});

//各级栏目联动函数
function linkage(level){
    $(".firstClass").show();
    if(level==1){                          //栏目级别为1
        $("#firstClassText").show();
        $("#firstClassSelect").hide();
        $(".secondClass").hide();
        $(".thirdClass").hide();
    }
    else if(level==2){                     //栏目级别为2
        $("#firstClassText").hide();
        $("#firstClassSelect").show();
        $(".secondClass").show();
        $("#secondClassText").show();
        $("#secondClassSelect").hide();
        $(".thirdClass").hide();
    }
    else if(level==3){                     //栏目级别为3
        $("#firstClassText").hide();
        $("#firstClassSelect").show();
        $(".secondClass").show();
        $("#secondClassText").hide();
        $("#secondClassSelect").show();
        $(".thirdClass").show();
    }
    else{                                  //点击请选择是刷新界面
        window.location.reload(true);
    }
}

//加载二级栏目
$("body").on("change","#firstClassSelect",function () {
   $.post("getClassification",{"parentDirectory":$("#firstClassSelect").val()},function (data) {
       var jsonData = $.parseJSON(data);
       var str = "<option value='0'>请选择</option>";
       for(var i in jsonData){
           str+="<option value="+jsonData[i].classificationId+">"+jsonData[i].classificationName+"</option>";
       }
       $("#secondClassSelect").empty().append(str);
   });
});


//添加栏目
$("body").on("click","#add",function(){
    saveClassification();
});

//保存栏目
function saveClassification(){
    $("#classForm").attr("action", "saveClassification");
    $.ajaxSetup({});
    $("#classForm").ajaxSubmit({
        resetForm:false,
        dataType:'html',
        success:function(data){
            if(data==1){
                alert("操作成功!");
                location.href="/cms/classificationList";
            }
            else{
                alert("操作失败!");
                return false;
            }
        }
    });
}
