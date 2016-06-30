$('.collapsible').collapsible({
	accordion: false // A setting that changes the collapsible behavior to expandable instead of the default accordion style
});

$('.edit-column').click(function() {
	var num = $(this).data("column_id");
	var columnId = "#column" + num;
	$(columnId).attr("contenteditable", "true");
	$(columnId).focus();
	var preContent = $(columnId).text();
	var isSaved = false;
	$(columnId).blur(function() {
		var nowContent = $(columnId).text();
		dialog_show("提示", "名称已经改变，是否保存？", "保存", "取消");
		if (nowContent != preContent) {
			$("#dialog_btn1").unbind("click");
			$("#dialog").openModal({
				complete: function() {
					if (!isSaved) {
						$(columnId).text(preContent);
					}
					$('.lean-overlay').remove();
				}
			});
			$("#dialog_btn1").click(function() {
				isSaved = true;
				//TODO do sth to save
				Materialize.toast("保存成功", 2000);
			});
		}
		$(columnId).attr("contenteditable", "false");
	})
	event.stopPropagation();
});

$('.delete_column').click(function() {
	var num = $(this).data("column_id");
	var columnId = "#column" + num;
	var content = "删除" + $(columnId).text() + "，该栏目的文章也将一同删除，是否确认？"
	dialog_show("警告", content, "确认", "取消");
	$("#dialog_btn1").unbind("click");
	$("#dialog").openModal({
		complete: function() {
			$('.lean-overlay').remove();
		}
	});
	$("#dialog_btn1").click(function() {
		//TODO do sth to delete
		Materialize.toast("删除成功", 2000);
	});
	event.stopPropagation();
});

$(".delete_blog").click(function() {
	dialog_show("警告", "确认删除该篇blog？", "确认", "取消");
	$("#dialog_btn1").unbind("click");
	$("#dialog").openModal({
		complete: function() {
			$('.lean-overlay').remove();
		}
	});
	$("#dialog_btn1").click(function() {
		//TODO do sth to delete
		Materialize.toast("删除成功", 2000);
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

$('#add_column').click(function() {
	$("#column_add_save").unbind("click");
	$("#dialog_add_column").openModal({
		complete: function() {
			$('.lean-overlay').remove();
		}
	});
	$('#dialog_input').focus();
	$("#column_add_save").click(function() {
		Materialize.toast("添加成功", 2000);
	});
})