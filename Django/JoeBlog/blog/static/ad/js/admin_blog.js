var confirm = $('#dialog_btn1');
var overlay = $('.lean-overlay');

$(function () {
    $.ajaxSetup({headers: {"X-CSRFToken": getCookie("csrftoken")}});
});
function getCookie(name) {
    var arr, reg = new RegExp("(^| )" + name + "=([^;]*)(;|$)");
    if (arr = document.cookie.match(reg))
        return unescape(arr[2]);
    else
        return null;
}

$('.collapsible').collapsible({
    accordion: false // A setting that changes the collapsible behavior to expandable instead of the default accordion style
});


$('#add_column').click(function () {
    $("#column_add_save").unbind("click");
    $("#dialog_add_column").openModal({
        complete: function () {
            overlay.remove();
        }
    });
    $('#dialog_input').focus();
    $("#column_add_save").click(function () {
        var name = $('#dialog_input').val();
        $.post("blogs/addColumn",
            {
                name: name
            }, function (data) {
                Materialize.toast(data, 1000, '', function () {
                    if (data == "success") {
                        window.location.reload()
                    }
                });
            });
    });
})

$('.edit-column').click(function () {
    var num = $(this).data("column_id");
    var columnId = "#column" + num;
    $(columnId).attr("contenteditable", "true");
    $(columnId).focus();
    var preContent = $(columnId).text();
    var isSaved = false;
    $(columnId).blur(function () {
        var nowContent = $(columnId).text();
        dialog_show("提示", "名称已经改变，是否保存？", "保存", "取消");
        if (nowContent != preContent) {
            confirm.unbind("click");
            $("#dialog").openModal({
                complete: function () {
                    if (!isSaved) {
                        $(columnId).text(preContent);
                    }
                    overlay.remove();
                }
            });
            confirm.click(function () {
                isSaved = true;
                $.post("blogs/renameColumn",
                    {
                        columnId: num,
                        newName: nowContent
                    },
                    function (data) {
                        Materialize.toast(data, 1000, '', function () {
                            if (data == "success") {
                                window.location.reload()
                            }
                        });
                    });
            });
        }
        $(columnId).attr("contenteditable", "false");
    });
    event.stopPropagation();
});

$('.delete_column').click(function () {
    var num = $(this).data("column_id");
    var columnId = "#column" + num;
    var content = "删除" + $(columnId).text() + "，该栏目的文章也将一同删除，是否确认？";
    dialog_show("警告", content, "确认", "取消");
    confirm.unbind("click");
    $("#dialog").openModal({
        complete: function () {
            overlay.remove();
        }
    });
    confirm.click(function () {
        $.post("blogs/deleteColumn",
            {
                columnId: num
            },
            function (data) {
                Materialize.toast(data, 1000, '', function () {
                    if (data == "success") {
                        window.location.reload()
                    }
                });
            });
    });
    event.stopPropagation();
});

$(".blog-add").click(function () {
    var type = "add";
    var column_id = $(this).data("column_id");
    location.href = "blogs/editBlog?type=" + type + "&column_id=" + column_id;
});

$(".edit_blog").click(function () {
    var type = "edit";
    var column_id = $(this).data("column_id");
    var blog_id = $(this).data("blog_id");
    location.href = "blogs/editBlog?type=" + type + "&column_id=" + column_id + "&blog_id=" + blog_id;
});

$(".delete_blog").click(function () {
    var num = $(this).data("blog_id");
    dialog_show("警告", "确认删除该篇blog？", "确认", "取消");
    confirm.unbind("click");
    $("#dialog").openModal({
        complete: function () {
            overlay.remove();
        }
    });
    confirm.click(function () {
        $.post("blogs/deleteBlog",
            {
                blogId: num
            },
            function (data) {
                Materialize.toast(data, 1000, '', function () {
                    if (data == "success") {
                        window.location.reload()
                    }
                });
            });
    });
    event.stopPropagation();
});

/**
 * 更改dialog显示内容
 * @param {Object} title
 * @param {Object} content
 * @param {Object} btn1
 * @param {Object} btn2
 */
function dialog_show(title, content, btn1, btn2) {
    $("#dialog_title").text(title);
    $("#dialog_content").text(content);
    $("#dialog_btn1").text(btn1);
    $("#dialog_btn2").text(btn2);
};