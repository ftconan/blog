$(function(){
    classificationList();     //加载栏目列表
});

//加载栏目列表
function classificationList(){
    $.post("getClassificationList",function(data){
       var jsonData = $.parseJSON(data);
       var str = "";
       for(var i in jsonData){
           str+= "<tr><td>"+jsonData[i].classificationIdLevel+"</td>";
           str+="<td>"+jsonData[i].classificationName+"</td>";
           str+="<td>"+jsonData[i].parentDirectory+"</td>";
           str+="<td>"+jsonData[i].classificationOrder+"</td>";
           str+="<td>"+jsonData[i].isShow+"</td>";
           str+="<td><a class='edit' href='/cms/addClassification?update="+jsonData[i].classificationId+"' data-toggle='modal' id='"+jsonData[i].classificationId+"'><i class='fa fa-edit' title='修改'></i> 修改</a> <a class='delete' href='#' data-toggle='modal' id='"+jsonData[i].classificationId+"'><i class='fa fa-times' title='删除'></i> 删除</a></td></tr>";
       }
       $(".classificationList").empty().append(str);
    });
}

//删除栏目
$("body").on("click",".delete",function(data){
   var classificationId = $(this).attr("id");
    $("#classificationId").val(classificationId);
   if(confirm("确定要删除该条数据?")){
       $.post("deleteClassification",{"classificationId": classificationId},function(data){
           if(data){
               alert("删除成功!");
               location.reload(true);
           }
           else{
               alert("删除失败!");
               return false;
           }
       });
   }
   classificationList();
});
