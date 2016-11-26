$(function(){
    pictureList(); //加载图片列表
});

//加载图片列表
function pictureList(){
    $.post("getPictureList",function(data){
       var jsonData = $.parseJSON(data);
        var str = "";
        for(var i in jsonData) {
            str += "<tr><td id='"+jsonData[i].classificationId+"'>" + jsonData[i].classificationName + "</td>";
            str += "<td>" + jsonData[i].pictureName + "</td>";
            str+="<td>"+jsonData[i].createTime+"</td>";
            str+="<td>"+jsonData[i].isShow+"</td>";
            str+="<td><a class='edit' href='/cms/addPicture?update="+jsonData[i].pictureId+"' data-toggle='modal' id='"+jsonData[i].pictureId+"'><i class='fa fa-edit' title='修改'></i> 修改</a> <a class='delete' href='#' data-toggle='modal' id='"+jsonData[i].pictureId+"'><i class='fa fa-times' title='删除'></i> 删除</a></td></tr>";
        }
        $(".pictureList").empty().append(str);
    });
}

//删除图片
$("body").on("click",".delete",function(){
   var pictureId = $(this).attr("id");
    $("#pictureId").val(pictureId);
    if(confirm("确定要删除该条数据?")){
        $.post("deletePicture",{"pictureId":pictureId},function(data){
           if(data){
               alert("删除成功!");
               location.reload(true);
           }
           else{
               alert("删除成功!");
               return false;
           }
        });
    }
    pictureList();
});