$(function(){
    $("#uploadPicture").click(function(){            //点击上传按钮相当于点击了file按钮
        $("#pictureUrl").click();
    });
    $("#pictureUrl").on("change",function(e){
        var name = e.currentTarget.files[0].name;   //e.currentTarget.files 是一个数组，如果支持多个文件，则需要遍历
        $("#pictureName").val(name);                 //将上传图片名添加到文本框中
    });
    $("#pictureUrl").change(function () {           //在img加入图片
        $("#imgName").attr("src",getFileUrl("pictureUrl"));
    });
});

//加载二级栏目
$("body").on("change","#firstClassification",function () {
   $.post("getClassification",{"parentDirectory":$("#firstClassification").val()},function (data) {
       var jsonData = $.parseJSON(data);
       var str = "<option value='0'>请选择</option>";
       for(var i in jsonData){
           str+="<option value="+jsonData[i].classificationId+">"+jsonData[i].classificationName+"</option>";
       }
       $("#secondClassification").empty().append(str);
   });
});

//加载三级级栏目
$("body").on("change","#secondClassification",function () {
   $.post("getClassification",{"parentDirectory":$("#secondClassification").val()},function (data) {
       var jsonData = $.parseJSON(data);
       var str = "";
       for(var i in jsonData){
           str+="<option value="+jsonData[i].classificationId+">"+jsonData[i].classificationName+"</option>";
       }
       $("#thirdClassification").empty().append(str);
   });
   setTimeout(function(){                                     //setTimeout让数据
       if($("#thirdClassification").val()!=null){          //三级栏目中有内容
           $(".thirdClass").show();
       }
       else{
           $(".thirdClass").hide();
       }
       },100)
});

//发布博文
$("body").on("click","#saveNews",function(){
   if($("#saveNews").text()=="发布"){                      //text()获取html中的文本
       var status = $("#saveNews").attr("id");             //js1.1版本不支持this属性
       $("input[name='status']").val(status);              //新闻状态
       saveNews();
   }
});

//暂存博文
$("body").on("click","#laterSave",function(){
   var status = $("#laterSave").attr("id");
   $("input[name='status']").val(status);              //新闻状态
   saveNews();
});

//保存博文
function saveNews(){
    var content = $("#content").html();                 //新闻内容(html()存储html代码)
    $("#newsContent").val(content);
    $("#newsForm").attr("action", "saveNews");
    $.ajaxSetup({});
    $("#newsForm").ajaxSubmit({
        resetForm:false,
        dataType:'html',
        success:function (data) {
            if(data==0){
                alert("操作失败!");
                return false;
            }
            else if(data==1){
                alert("操作成功!");
                location.href="/cms/newsList";
            }
            else if(data==2){
                alert("操作成功!");
                location.href="/cms/newsList";
            }
        }
    });
}

//从本地获取input[file]图片的url Important
function getFileUrl(fileId) {
    var url;
    var file = document.getElementById(fileId);
    var agent = navigator.userAgent;
    if (agent.indexOf("MSIE")>=1) {
    url = file.value;
    } else if(agent.indexOf("Firefox")>0) {
    url = window.URL.createObjectURL(file.files.item(0));
    } else if(agent.indexOf("Chrome")>0) {
    url = window.URL.createObjectURL(file.files.item(0));
    }
    return url;
}

