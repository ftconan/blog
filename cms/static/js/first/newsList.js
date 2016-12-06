$(function(){
    newsList();       //加载新闻列表
});

//加载新闻列表
function newsList(){
    $.post("getNewsList",function(data){
       var jsonData = $.parseJSON(data);
        var str = "";
        for(var i in jsonData){
            str+="<tr><td>"+jsonData[i].parentDirectory+"</td>";
            str+="<td>"+jsonData[i].classificationName+"</td>";
            str+="<td>"+jsonData[i].title+"</td>";
            str+="<td>"+jsonData[i].createTime+"</td>";
            str+="<td>"+jsonData[i].isTop+"</td>";
            str+="<td><a class='edit' href='/cms/addNews?update="+jsonData[i].newsId+"' data-toggle='modal' id='"+jsonData[i].newsId+"'><i class='fa fa-edit' title='修改'></i> 修改</a> <a class='delete' href='#' data-toggle='modal' id='"+jsonData[i].newsId+"'><i class='fa fa-times' title='删除'></i> 删除</a></td></tr>";
        }
        $(".newsList").empty().append(str);
    });
}

//删除新闻
$("body").on("click",".delete",function(data){
    var newsId = $(this).attr("id");
    $("#newsId").val(newsId);
    if(confirm("确定要删除该条数据?")){
        $.post("deleteNews",{"newsId": newsId},function(data){
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
});
