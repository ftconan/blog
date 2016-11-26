$(function(){
    accountList();       //加载账号列表
});

//加载账号列表
function accountList(){
    $.post("getAccountList",function(data){
        var jsonData = $.parseJSON(data);
        var str = "";
        for(var i in jsonData){
            str+="<tr><td>"+jsonData[i].userName+"</td>";
            str+="<td>"+jsonData[i].userAccount+"</td>";
            str+="<td>"+jsonData[i].password+"</td>";
            str+="<td>"+jsonData[i].isShow+"</td>";
            str+="<td><a class='edit' href='/cms/addAccount?update="+jsonData[i].userId+"' data-toggle='modal' id='"+jsonData[i].userId+"'><i class='fa fa-edit' title='修改'></i> 修改</a> <a class='delete' href='#' data-toggle='modal' id='"+jsonData[i].userId+"'><i class='fa fa-times' title='删除'></i> 删除</a></td></tr>";
        }
        $(".accountList").empty().append(str);
    });
}

//删除账号
$("body").on("click",".delete",function(){
   var userId = $(this).attr("id");
    $("#userId").val(userId);
    if(confirm("确定要删除该条数据?")){
        $.post("deleteAccount",{"userId":userId},function(data){
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
    accountList();
});