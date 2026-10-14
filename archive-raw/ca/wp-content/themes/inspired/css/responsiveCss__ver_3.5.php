/* Responsive Reset */
img {
	max-width: 100%;
	height: auto;
}
.responsiveImage{
	display: block;
	margin-left: auto;
	margin-right: auto;
}
.googleMap img, .kwicks img, .anythingImage{
	max-width: none;
}


/* ----------------------------------------------------- */
/* Tablet (Portrait) */
/* ----------------------------------------------------- */
/* Width of 768px */
/* ----------------------------------------------------- */

@media only screen and (min-width: 768px) and (max-width: 989px) {
	#wrapper{
		width: 728px;
	}
	#content.noSideBar{
		width: 728px;
	}
	#content.leftSideBar{
		float: right;
		width: 515px;
	}
	#content.rightSideBar{
		float: left;
		width: 515px;
	}
	#content.noSideBar .portInnerFullWidth{
		width: 668px;
	}
	#content.leftSideBar .portInnerFullWidth, #content.rightSideBar .portInnerFullWidth{
		width: 455px;
	}
	#content.noSideBar .portInnerOneThird{
		width: 209px;
	}
	#content.leftSideBar .portInnerOneThird, #content.rightSideBar .portInnerOneThird{
		width: 138px;
		margin-right: 0px;
	}
	#content.noSideBar .portInnerOneHalf{
		width: 324px;
	}
	#content.leftSideBar .portInnerOneHalf, #content.rightSideBar .portInnerOneHalf{
		width: 217px;
	}
	#content.noSideBar .portInnerOneFourth{
		width: 152px;
	}
	#content.leftSideBar .portInnerOneFourth, #content.rightSideBar .portInnerOneFourth{
		width: 98px;
	}
	#preHeader{
		width: 728px;
	}
	#header{
		width: 728px;
	}
	#pageTitle{
		width: 606px;
	}
	#sideBar{
		width: 181px;
	}
	#sideBarWidgets .nameInput, #sideBarWidgets .emailInput, #sideBarWidgets .messageInput {
		width: 90%;
	}
	#footer {
		width: 728px;
	}
	#postFooter{
		width:688px;
	}
	#postFooterContent{
		width:688px;
	}
	
	#content.noSideBar .fullWidth{
		width: 668px;
	}
	#content.noSideBar .outerOneHalf{
		width: 324px;
	}
	#content.noSideBar .outerOneThird{
		width: 209px;
	}
	#content.noSideBar .outerTwoThirds{
		width: 439px;
	}
	#content.noSideBar .outerOneFourth{
		width: 152px;
	}
	#content.noSideBar .outerThreeFourths{
		width: 496px;
	}
	#content.noSideBar .outerOneFifth{
		width: 117px;
	}
	#content.noSideBar .outerFourFifths{
		width: 531px;
	}
	#content.noSideBar .outerOneSixth{
		width: 94px;
	}
	#content.noSideBar .outerFiveSixths{
		width: 554px;
	}

	
	/* Left SideBar and Right SideBar Columns */
	#content.leftSideBar .fullWidth, #content.rightSideBar .fullWidth{
		width: 455px;
	}
	#content.leftSideBar .outerOneHalf, #content.rightSideBar .outerOneHalf{
		width: 217px;
	}
	#content.leftSideBar .outerOneThird, #content.rightSideBar .outerOneThird{
		width: 138px;
	}
	#content.leftSideBar .outerTwoThirds, #content.rightSideBar .outerTwoThirds{
		width: 297px;
	}
	#content.leftSideBar .outerOneFourth, #content.rightSideBar .outerOneFourth{
		width: 98px;
	}
	#content.leftSideBar .outerThreeFourths, #content.rightSideBar .outerThreeFourths{
		width: 337px;
	}
	#content.leftSideBar .outerOneFifth, #content.rightSideBar .outerOneFifth{
		width: 75px;
	}
	#content.leftSideBar .outerFourFifths, #content.rightSideBar .outerFourFifths{
		width: 360px;
	}
	#content.leftSideBar .outerOneSixth, #content.rightSideBar .outerOneSixth{
		width: 59px;
	}
	#content.leftSideBar .outerFiveSixths, #content.rightSideBar .outerFiveSixths{
		width: 376px;
	}
	
	#footer .fullWidth{
		width: 728px;
	}
	#footer .outerOneHalf{
		width: 364px;
	}
	#footer .outerOneThird{
		width: 242px;
	}
	#footer .outerTwoThirds{
		width: 486px;
	}
	#footer .outerOneFourth{
		width: 182px;
	}
	#footer .outerThreeFourths{
		width: 546px;
	}
	#footer .outerOneFifth{
		width: 145px; 
	}
	#footer .outerFourFifths{
		width: 583px;
	}
	#footer .outerOneSixth{
		width: 121px;
	}
	#footer .outerFiveSixths{
		width: 607px;
	}
	
	.widgetRecentPost .innerOneThird{
		/*display: none;*/
	}
	.widgetRecentPost .innerTwoThirds{
		/*width: 100%;
		float: none;*/
	}
	/* WordPress Search Widget */
	.widget_search .screen-reader-text {
		display: none;
	}
	#searchform div{
		width: 141px;
		height: 33px;
		background-repeat: no-repeat;
		background-position: 0 0;
	}
	#s{
		display: inline;
		float: left;
		padding: 0 8px;
		width: 87px;
		height: 33px;
		line-height: 33px;
		border: none;
		outline: none;
		opacity: 0;
		filter: alpha(opacity = 0);
		background-repeat: no-repeat;
		background-position: 0 0;
	}
	#searchsubmit{
		display: inline;
		float: left;
		width: 38px;
		height: 33px;
		border: none;
		outline: none;
		cursor: pointer;
		background-repeat: no-repeat;
		background-position: 0 0;
	}
	
	/* Custom Widgets */
	#sideBarWidgets .widgetRecentPost .thumbHolder, #footer .widgetRecentPost .thumbHolder {
		display: none;
	}
	#sideBarWidgets .widgetRecentPost .textHolder, #footer .widgetRecentPost .textHolder {
		width: 100%;
	}
	.buttonsColumn1{
		margin-bottom: 10px;
	}
	.theLayerSlider, .carousel, .anythingOuterWrap, .kwicksOuterWrap, .nivoOuterWrap, .pieceMaker1OuterWrap, .pieceMaker2OuterWrap{
		display:none !important;
	}
	.layerSliderFallBack, .carouselFallBack, .anythingFallBack, .kwicksFallBack, .nivoFallBack, .pieceMaker1FallBack, .pieceMaker2FallBack{
		display:block !important;
	}
}

/* Mobile Landscape Size to Tablet Portrait (devices and browsers) */
@media only screen and (min-width: 480px) and (max-width: 767px) {
	#wrapper{
		width: 420px;
		top: 0px;
		margin-bottom: 40px;
	}
	#pageContent{
		padding: 20px;
	}
	#content.noSideBar{
		width: 420px;
	}
	#content.leftSideBar{
		float: right;
		width: 420px;
	}
	#content.rightSideBar{
		float: left;
		width: 420px;
	}
	#preHeader{
		
		width: 420px;
		padding-top: 10px;
		padding-bottom: 10px;
		height: auto;
	}
	#preHeaderContent{
		display:block;
		height: auto;
		-webkit-text-size-adjust:none;
	}
	#preHeaderContent ul li a {
		-webkit-text-size-adjust:none;
	}
	#preHeaderLeft{
		display:block;
		text-align:center;
	}
	#preHeaderRight{
		display:block;
		text-align: center;
	}
	.phoneNumber{
		padding-right:5px;
		float:none;
		display: inline;
	}
	.emailAddress{
		float:none;
		display: inline;
	}
	#preHeaderRightContent {
		float: none;
	}
	#preHeader ul li {
		float: none;
	}
	#header{
		width: 420px;
		height: 164px;
	}
	#headerSocial{
		
		top: 20px;
		right: 20px;
		z-index: 2;
	}
	#horizontalLogo{
		top: 30px;
		left: 20px;
	}
	#headerSearch {
		display: none;
		position: absolute;
		top: 142px;
		left: 20px;
		margin-bottom: 0px;
	}
	#searchWrap{
		display: block;
	}
	.searchTitle{
		display: none;
	}
	.searchCaption{
		display: block;
		width: 220px;
		padding-right: 0px;
		margin-bottom: 5px;
	}
	.headerSearchBox{
		display: block;
	}
	#navWrap{
		display: none;
	}
	.custom-select{
		display: block;
		left: 20px;
		top: 129px;
		bottom: auto;
	}
	.custom-select select {
		width:380px;
	}
	#featuredArea{
		padding-top: 20px;
	}
	#titleWrapper{
		padding-top: 20px;
		margin-left: 20px;
	}
	#pageTitle{
		width: 338px;
		padding: 20px 20px;
		text-align: center;
	}
	#title{
		text-align: left !important;
	}
	/* No SideBar Left SideBar and Right SideBar Columns */
	#content.noSideBar .fullWidth, #content.leftSideBar .fullWidth, #content.rightSideBar .fullWidth, #content.noSideBar .outerOneHalf, #content.leftSideBar .outerOneHalf, #content.rightSideBar .outerOneHalf,
	#content.noSideBar .outerOneThird, #content.leftSideBar .outerOneThird, #content.rightSideBar .outerOneThird, #content.noSideBar .outerTwoThirds, #content.leftSideBar .outerTwoThirds, #content.rightSideBar .outerTwoThirds,
	#content.noSideBar .outerOneFourth, #content.leftSideBar .outerOneFourth, #content.rightSideBar .outerOneFourth, #content.noSideBar .outerThreeFourths, #content.leftSideBar .outerThreeFourths, #content.rightSideBar .outerThreeFourths,
	#content.noSideBar .outerOneFifth, #content.leftSideBar .outerOneFifth, #content.rightSideBar .outerOneFifth, #content.noSideBar .outerFourFifths, #content.leftSideBar .outerFourFifths, #content.rightSideBar .outerFourFifths,
	#content.noSideBar .outerOneSixth, #content.leftSideBar .outerOneSixth, #content.rightSideBar .outerOneSixth, #content.noSideBar .outerFiveSixths, #content.leftSideBar .outerFiveSixths, #content.rightSideBar .outerFiveSixths{
		width: 380px;
		padding-bottom: 20px;
		border-bottom: 1px dotted #E4E4DA;
		margin-bottom: 20px;
	}
	.backToTop{
		margin-top: -15px !important;
		margin-bottom: 20px;
	}
	.hrWrap{
		display: none;
	}
	#sideBar{
		display:none;
		width: 420px;
		margin-top: 0px;
		padding-top: 10px;
	}
	#sideBar.rightSideBar{
		margin-right: 0px;
		margin-bottom: 0px;
		border-left: none;
		border-right: none;
		border-bottom: none;
		-webkit-border-radius: 0px;
		-moz-border-radius: 0px;
		border-radius: 0px;
	}
	#sideBar.leftSideBar{
		margin-left: 0px;
		margin-bottom: 0px;
		border-left: none;
		border-right: none;
		border-bottom: none;
		-webkit-border-radius: 0px;
		-moz-border-radius: 0px;
		border-radius: 0px;
	}
	#sideBarWidgets{
		padding-bottom: 30px;
	}
	#portfolioGrid {
		margin-left: 0px;
		overflow: visible !important;
	}
	#content.noSideBar .portInnerFullWidth, #content.leftSideBar .portInnerFullWidth, #content.rightSideBar .portInnerFullWidth,
	#content.noSideBar .portInnerOneThird, #content.leftSideBar .portInnerOneThird, #content.rightSideBar .portInnerOneThird,
	#content.noSideBar .portInnerOneHalf, #content.leftSideBar .portInnerOneHalf, #content.rightSideBar .portInnerOneHalf,
	#content.noSideBar .portInnerOneFourth, #content.leftSideBar .portInnerOneFourth, #content.rightSideBar .portInnerOneFourth{
		width: 380px;
		margin-left: 0px !important;
	}
	.portInnerFullWidth .outerTwoThirds, .portInnerFullWidth .outerOneThird{
		padding-bottom: 0px !important;
		border: none !important;
		margin-bottom: 0px !important;
	}
	.contactFormBorder{
		padding: 20px;
	}
	
	/* Flex Slider Styles */
	.flex-control-nav{
		display:none;
	}
	.flex-direction-nav{
		
	}
	.flex-caption{
		display:none;
	}
	.flex-big-caption{
		display:none;
	}
	
	/* Footer General Styles */
	#footer{
		display: block;
		width: 420px;
		padding-bottom: 30px;
	}
	#footer .fullWidth, #footer .outerOneHalf, #footer .outerOneThird, #footer .outerTwoThirds, #footer .outerOneFourth,
	#footer .outerThreeFourths, #footer .outerOneFifth, #footer .outerFourFifths, #footer .outerOneSixth, #footer .outerFiveSixths{
		display: inline;
		float: left;
		width: 420px;
		background-image: none;
		clear:right;
	}
	#footer p {
		line-height: 19px;
	}
	#footer .smallBorder {
		padding: 5px;
	}
	#footer .columnShadow{
		background-image: none;
		margin-bottom: 30px;
		height: 1px;
	}
	#footer .first .columnShadow, #footer .fullWidth .columnShadow{
		background-image: url(http://www.cainversiones.com/ca/wp-content/themes/inspired/images/skins/cream/footerShadow.png);
		margin-left: 0px;
		margin-right: 0px;
		border-bottom: none;
		height: 5px;
	}
	#footer .widget {
		background-position: 0px 0px;
		padding-bottom: 0px;
	}
	
	/* RECENT POSTS WIDGET */
	#footer .widgetRecentPost {
		margin-bottom: 20px;
	}
	#footer .widget_wb_recent_posts .innerOneThird{
		/*display: none;*/
	}
	#footer .widget_wb_recent_posts .innerTwoThirds{
		/*width: 100%;
		float: none;*/
	}
	
	/* CONTACT INFO WIDGET */
	#footer .infoC1, #footer .infoC2{
		margin-bottom: 20px;
	}
	.contactInfo {
		margin-bottom: 0px;
	}
	
	/* CONTACT FORM WIDGET */
	#footer .nameInput, #footer .emailInput{
		width: 80%;
	}
	#footer .messageInput {
		width: 96%;
	}
	
	/* TWITTER WIDGET */
	.tweet{
		width:auto;
	}
	.tweet_odd, .tweet_even{
		width: auto;
		margin-bottom: 20px;
	}
	
	/* POST FOOTER STYLES */
	#postFooter{
		width:380px;
	}
	#postFooterContent{
		width:380px;
	}
	#copyright{
		float: none;
		text-align: center;
	}
	#post_footer_widget_area{
		display: block;
		float: none;
		text-align: center;
	}
	#postFooterContent ul li{
		float: none;
		display: inline;
	}
	.list-o-comments ul{
		margin-left: 0px;
	}
	.buttonsColumn1 a.button, .buttonsColumn2 a.button {
		margin-right: 10px;
	}
	.buttonsColumn1{
		float: left;
		margin-right: 0px;
		margin-bottom: 10px;
	}
	.oneThirdPriceColumn{
		float: none;
		width: 378px;
		padding-bottom: 20px;
		border-bottom: 1px dotted #E4E4DA;
		margin-bottom: 20px;
	}
	.oneFourthPriceColumn{
		float: none;
		width: 378px;
		padding-bottom: 20px;
		border-bottom: 1px dotted #E4E4DA;
		margin-bottom: 20px;
	}
	.pricingBox.lightPriceTable.featured,.pricingBox.darkPriceTable.featured{
		width: 378px;
		margin-top: 0px;
		margin-left: 0;
	}
	.theLayerSlider, .carousel, .anythingOuterWrap, .kwicksOuterWrap, .nivoOuterWrap, .pieceMaker1OuterWrap, .pieceMaker2OuterWrap{
		display:none !important;
	}
	.layerSliderFallBack, .carouselFallBack, .anythingFallBack, .kwicksFallBack, .nivoFallBack, .pieceMaker1FallBack, .pieceMaker2FallBack{
		display:block !important;
	}
}


/* Mobile Portrait Size to Mobile Landscape (devices and browsers) */
@media only screen and (max-width: 479px) {
	#wrapper{
		width: 300px;
		top: 0px;
		margin-bottom: 0px;
	}
	#pageContent{
		padding: 20px;
	}
	#content.noSideBar{
		width: 300px;
	}
	#content.leftSideBar{
		float: right;
		width: 300px;
	}
	#content.rightSideBar{
		float: left;
		width: 300px;
	}
	#preHeader{
		display: none;
		width: 300px;
		padding-top: 10px;
		padding-bottom: 10px;
		height: auto;
	}
	#preHeaderContent{
		display:block;
		height: auto;
		-webkit-text-size-adjust:none;
	}
	#preHeaderContent ul li a {
		-webkit-text-size-adjust:none;
	}
	#preHeaderLeft{
		display: none;
		text-align:center;
	}
	#preHeaderRight{
		display: none;
		text-align: center;
	}
	.phoneNumber{
		padding-right:5px;
		float:none;
		display: inline;
	}
	.emailAddress{
		float:none;
		display: inline;
	}
	#preHeaderRightContent {
		float: none;
	}
	#preHeader ul li {
		float: none;
	}
	#header{
		width: 300px;
		height: 185px;
	}
	#headerSocial{
		
		top: 20px;
		right: 20px;
		z-index: 2;
	}
	#horizontalLogo{
		top: 53px;
		left: 45px;
	}
	#headerSearch {
		display: none;
		position: absolute;
		top: 142px;
		left: 20px;
		margin-bottom: 0px;
	}
	#searchWrap{
		display: block;
	}
	.searchTitle{
		display: none;
	}
	.searchCaption{
		display: block;
		width: 220px;
		padding-right: 0px;
		margin-bottom: 5px;
	}
	.headerSearchBox{
		display: block;
	}
	#navWrap{
		display: none;
	}
	.custom-select{
		display: block;
		left: 20px;
		top: 148px;
		bottom: auto;
	}
	.custom-select select {
		width:260px;
	}
	#featuredArea{
		padding-top: 20px;
	}
	#titleWrapper{
		padding-top: 20px;
		margin-left: 20px;
	}
	#pageTitle{
		width: 218px;
		padding: 20px 20px;
		text-align: center;
	}
	#title{
		text-align: left !important;
	}
	/* No SideBar Left SideBar and Right SideBar Columns */
	#content.noSideBar .fullWidth, #content.leftSideBar .fullWidth, #content.rightSideBar .fullWidth, #content.noSideBar .outerOneHalf, #content.leftSideBar .outerOneHalf, #content.rightSideBar .outerOneHalf,
	#content.noSideBar .outerOneThird, #content.leftSideBar .outerOneThird, #content.rightSideBar .outerOneThird, #content.noSideBar .outerTwoThirds, #content.leftSideBar .outerTwoThirds, #content.rightSideBar .outerTwoThirds,
	#content.noSideBar .outerOneFourth, #content.leftSideBar .outerOneFourth, #content.rightSideBar .outerOneFourth, #content.noSideBar .outerThreeFourths, #content.leftSideBar .outerThreeFourths, #content.rightSideBar .outerThreeFourths,
	#content.noSideBar .outerOneFifth, #content.leftSideBar .outerOneFifth, #content.rightSideBar .outerOneFifth, #content.noSideBar .outerFourFifths, #content.leftSideBar .outerFourFifths, #content.rightSideBar .outerFourFifths,
	#content.noSideBar .outerOneSixth, #content.leftSideBar .outerOneSixth, #content.rightSideBar .outerOneSixth, #content.noSideBar .outerFiveSixths, #content.leftSideBar .outerFiveSixths, #content.rightSideBar .outerFiveSixths{
		width: 260px;
		padding-bottom: 20px;
		border-bottom: 1px dotted #E4E4DA;
		margin-bottom: 20px;
	}
	.backToTop{
		margin-top: -15px !important;
		margin-bottom: 20px;
	}
	.hrWrap{
		display: none;
	}
	#sideBar{
		display:none;
		width: 300px;
		margin-top: 0px;
		padding-top: 10px;
	}
	#sideBar.rightSideBar{
		margin-right: 0px;
		margin-bottom: 0px;
		border-left: none;
		border-right: none;
		border-bottom: none;
		-webkit-border-radius: 0px;
		-moz-border-radius: 0px;
		border-radius: 0px;
	}
	#sideBar.leftSideBar{
		margin-left: 0px;
		margin-bottom: 0px;
		border-left: none;
		border-right: none;
		border-bottom: none;
		-webkit-border-radius: 0px;
		-moz-border-radius: 0px;
		border-radius: 0px;
	}
	#sideBarWidgets{
		padding-bottom: 30px;
	}
	#portfolioGrid {
		margin-left: 0px;
		overflow: visible !important;
	}
	#content.noSideBar .portInnerFullWidth, #content.leftSideBar .portInnerFullWidth, #content.rightSideBar .portInnerFullWidth,
	#content.noSideBar .portInnerOneThird, #content.leftSideBar .portInnerOneThird, #content.rightSideBar .portInnerOneThird,
	#content.noSideBar .portInnerOneHalf, #content.leftSideBar .portInnerOneHalf, #content.rightSideBar .portInnerOneHalf,
	#content.noSideBar .portInnerOneFourth, #content.leftSideBar .portInnerOneFourth, #content.rightSideBar .portInnerOneFourth{
		width: 260px;
		margin-left: 0px !important;
	}
	.portInnerFullWidth .outerTwoThirds, .portInnerFullWidth .outerOneThird{
		padding-bottom: 0px !important;
		border: none !important;
		margin-bottom: 0px !important;
	}
	.contactFormBorder{
		padding: 20px;
	}
	
	/* Flex Slider Styles */
	.flex-control-nav{
		display:none;
	}
	.flex-direction-nav{
		
	}
	.flex-caption{
		display:none;
	}
	.flex-big-caption{
		display:none;
	}
	
	/* Footer General Styles */
	#footer{
		display: block;
		width: 300px;
		padding-bottom: 30px;
	}
	#footer .fullWidth, #footer .outerOneHalf, #footer .outerOneThird, #footer .outerTwoThirds, #footer .outerOneFourth,
	#footer .outerThreeFourths, #footer .outerOneFifth, #footer .outerFourFifths, #footer .outerOneSixth, #footer .outerFiveSixths{
		display: inline;
		float: left;
		width: 300px;
		background-image: none;
		clear:right;
	}
	#footer p {
		line-height: 19px;
	}
	#footer .smallBorder {
		padding: 5px;
	}
	#footer .columnShadow{
		background-image: none;
		margin-bottom: 30px;
		height: 1px;
	}
	#footer .first .columnShadow, #footer .fullWidth .columnShadow{
		background-image: url(http://www.cainversiones.com/ca/wp-content/themes/inspired/images/skins/cream/footerShadow.png);
		margin-left: 0px;
		margin-right: 0px;
		border-bottom: none;
		height: 5px;
	}
	#footer .widget {
		background-position: 0px 0px;
		padding-bottom: 0px;
	}
	
	/* RECENT POSTS WIDGET */
	#footer .widgetRecentPost {
		margin-bottom: 20px;
	}
	#footer .widget_wb_recent_posts .innerOneThird{
		/*display: none;*/
	}
	#footer .widget_wb_recent_posts .innerTwoThirds{
		/*width: 100%;
		float: none;*/
	}
	
	/* CONTACT INFO WIDGET */
	#footer .infoC1, #footer .infoC2{
		margin-bottom: 20px;
	}
	.contactInfo {
		margin-bottom: 0px;
	}
	
	/* CONTACT FORM WIDGET */
	#footer .nameInput, #footer .emailInput{
		width: 80%;
	}
	#footer .messageInput {
		width: 96%;
	}
	
	/* TWITTER WIDGET */
	.tweet{
		width:auto;
	}
	.tweet_odd, .tweet_even{
		width: auto;
		margin-bottom: 20px;
	}
	
	/* POST FOOTER STYLES */
	#postFooter{
		width:260px;
	}
	#postFooterContent{
		width:260px;
	}
	#copyright{
		float: none;
		text-align: center;
	}
	#post_footer_widget_area{
		display: block;
		float: none;
		text-align: center;
	}
	#postFooterContent ul li{
		float: none;
		display: inline;
	}
	.list-o-comments ul{
		margin-left: 0px;
	}
	.buttonsColumn1 a.button, .buttonsColumn2 a.button {
		margin-right: 0px;
	}
	.buttonsColumn1{
		float: left;
		margin-right: 0px;
		margin-bottom: 10px;
	}
	.oneThirdPriceColumn{
		float: none;
		width: 258px;
		padding-bottom: 20px;
		border-bottom: 1px dotted #E4E4DA;
		margin-bottom: 20px;
	}
	.oneFourthPriceColumn{
		float: none;
		width: 258px;
		padding-bottom: 20px;
		border-bottom: 1px dotted #E4E4DA;
		margin-bottom: 20px;
	}
	.pricingBox.lightPriceTable.featured,.pricingBox.darkPriceTable.featured{
		width: 258px;
		margin-top: 0px;
		margin-left: 0;
	}
	.theLayerSlider, .carousel, .anythingOuterWrap, .kwicksOuterWrap, .nivoOuterWrap, .pieceMaker1OuterWrap, .pieceMaker2OuterWrap{
		display:none !important;
	}
	.layerSliderFallBack, .carouselFallBack, .anythingFallBack, .kwicksFallBack, .nivoFallBack, .pieceMaker1FallBack, .pieceMaker2FallBack{
		display:block !important;
	}
}