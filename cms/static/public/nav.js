$(function(){
    $.post("getAdminName",function(data){          //传给getAdminName
        var str=data;
        $("#adminName").append(str);
    })
})