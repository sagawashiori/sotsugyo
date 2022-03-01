$(function(){


function twitText() {
	var s, url;
	s = "今の総アイテム数は◎個です";
	url = document.location.href;
	
	if (s != "") {
		if (s.length > 140) {
			//文字数制限
			alert("テキストが140字を超えています");
		} else {
			//投稿画面を開く
			url = "http://twitter.com/share?url=" + escape(url) + "&text=" + s;
			window.open(url,"_blank","width=600,height=300");
		}
	}
}
    
      
      $('.slide-wrap').slick({
        infinite: true,
        slidesToShow: 3,
        slidesToScroll: 3
      });


});