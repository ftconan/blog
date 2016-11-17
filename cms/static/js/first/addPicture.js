$(function(){
    getPicturePosition();                               //获取所属栏目
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

//获取所属栏目
function getPicturePosition(){
    $.post("getPicturePosition",function(data){
        var jsonData = $.parseJSON(data);
        var str = "";
        for(var i in jsonData){
            str+="<option value="+jsonData[i].classificationId+">"+"("+jsonData[i].classificationIdLevel+")"+ jsonData[i].classificationName+"</option>";
        }
        $("#picturePosition").append(str);
    });
}

//添加图片
$("body").on("click","#add",function () {
    savePicture();
});

//保存图片
function savePicture(){
    $("#pictureForm").attr("action","savePicture");
    $.ajaxSetup({});
    $("#pictureForm").ajaxSubmit({
        resetForm:false,
        dataType:'html',
        success:function (data) {
            if(data==1){
                alert("操作成功!");
                location.href="/cms/pictureList";
            }
            else{
                alert("操作失败!");
                return false;
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
