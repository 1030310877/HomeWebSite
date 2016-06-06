(function($) {
	var self;
	var nowYear;
	var nowMonth;
	var nowDay;
	var nowDayInWeek;
	$.fn.genCalendar = function(options) {
		self = $(this);
		var date = new Date();
		var defaults = {
			'year': date.getFullYear(),
			'month': date.getMonth(),
			'day': date.getDate()
		};
		var settings = $.extend(defaults, options);
		var content = "<div class=\"row\" style=\"width: 100%; margin-right: auto; min-height: 240px;background: transparent;\">";
		content += "<div id=\"monthcontainer\" class=\"col s3 m3 l3 month-container\">";
		content += "<div class=\"row\">";
		content += "<div id=\"years\" class=\"center col s12 m12 l12\" style=\"margin-top: 20px;\">2016</div>";
		content += "<div id=\"months\" class=\"center months col s12 m12 l12\" style=\"margin-top: 30px;\">";
		content += "<div class=\"month-unchecked\">&nbsp;</div>";
		content += "<div id=\"jan\" class=\"month month-checked\">Jan</div>";
		content += "<div id=\"feb\" class=\"month month-unchecked\">Feb</div>";
		content += "<div id=\"mar\" class=\"month month-unchecked\">Mar</div>";
		content += "<div id=\"apr\" class=\"month month-unchecked\">Apr</div>";
		content += "<div id=\"may\" class=\"month month-unchecked\">May</div>";
		content += "<div id=\"jun\" class=\"month month-unchecked\">Jun</div>";
		content += "<div id=\"jul\" class=\"month month-unchecked\">Jul</div>";
		content += "<div id=\"aug\" class=\"month month-unchecked\">Aug</div>";
		content += "<div id=\"sep\" class=\"month month-unchecked\">Sep</div>";
		content += "<div id=\"otc\" class=\"month month-unchecked\">Otc</div>";
		content += "<div id=\"nov\" class=\"month month-unchecked\">Nov</div>";
		content += "<div id=\"dec\" class=\"month month-unchecked\">Dec</div>";
		content += "<div class=\"month-unchecked\">&nbsp;</div></div></div></div>";
		content += "<table id=\"weeks\" class=\"col s9 m9 l9\"><tr><th>Sun</th><th>Mon</th><th>Tue</th><th>Wed</th><th>Thu</th><th>Fri</th><th>Sat</th></tr></table></div>";
		$(this).html(content);
		var unCheckHeight = $('.month-unchecked').height();
		var checkHeight = $('.month-checked').height();
		var monthcontentheight = unCheckHeight * 2 + checkHeight;
		$('#months').height(monthcontentheight);
		$('#months').mousewheel(function(event, delta, deltaX, deltaY) {
			var nowtop = $('#months').scrollTop();
			var toTop = nowtop + deltaY;
			if (toTop < 0) {
				return;
			}
			$('#months').scrollTop(toTop);
			var month = Math.floor(toTop / unCheckHeight);
			$(this).showDate(settings.year, month);
		})
		$('.month').each(function(month) {
			$(this).click(function() {
				chooseMonth(month);
				self.showDate(2016, month);
			});
		});
		chooseMonth(settings.month);
		self.showDate(settings.year, settings.month);
		var weekheight = $('#weeks').height();
		$('#monthcontainer').height(weekheight);
	};

	var chooseMonth = function(month) {
		$('.month').each(function() {
			$(this).removeClass("month-checked").addClass("month-unchecked");
		});
		$('.month').eq(month).removeClass("month-unchecked").addClass("month-checked");
		var unCheckHeight = $('.month-unchecked').height();
		$('#months').animate({
			scrollTop: month * unCheckHeight + 'px'
		}, 200);
	}

	$.fn.showDate = function(year, month) {
		if (month >= 0 && month <= 11) {
			$('.month').each(function() {
				$(this).removeClass("month-checked").addClass("month-unchecked");
			});
			$('.month').eq(month).removeClass("month-unchecked").addClass("month-checked");
			var mdate = new Date();
			mdate.setMonth(month + 1);
			mdate.setDate(0);
			var days = mdate.getDate();
			var ndate = new Date(); //不new将会导致日期不正确
			ndate.setYear(year);
			ndate.setMonth(month);
			ndate.setDate(1);
			var first = ndate.getDay();
			var content = "<tr><th>Sun</th><th>Mon</th><th>Tue</th><th>Wed</th><th>Thu</th><th>Fri</th><th>Sat</th></tr>";
			var j = 0;
			for (var i = 0; i < days + first; i++) {
				if (i % 7 == 0) {
					content = content + "<tr>";
				}
				content = content + "<td>";
				if (i >= first) {
					content = content + (i + 1 - first);
				}
				content = content + "</td>";
				if (i % 7 == 6) {
					content = content + "</tr>";
				}
			}
			$('#weeks').html(content);
			var weekheight = $('#weeks').height();
			$('#monthcontainer').height(weekheight);
		}
	}
})(jQuery);