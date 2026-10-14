jQuery.noConflict();

jQuery(document).ready(function($) {

	if ($(".portInnerFullWidth").length > 0){
		$("#portfolioGrid").css('margin-left','0px');
	}
	$(window).resize(function() {
		var $portfolioGrid = $('#portfolioGrid');
		$portfolioGrid.isotope({
			itemSelector : '.element',
			resizable : true,
			resizesContainer : true,
			containerStyle : { position: 'relative', overflow: 'hidden' },
			transformsEnabled : true,
			layoutMode : 'fitRows'
		});
	});	
	
	//Main Navigation Menu Activation
	$('#navWrap ul.sf-menu').superfish();
	
	//Accordion SideBar Menu Activation
	$("#sideBar .widget_nav_menu ul li").menu();
	$("#footer .widget_nav_menu ul li").menu();
	
	//Social Icon Opacity Animation
	$('.socialIcons li').each(function(index) {
		$(this).hover(
		  function () {
			if(typeof document.documentElement.style.opacity!='undefined'){
				$(this).animate({opacity: socialActiveAlpha});
			}
		  }, 
		  function () {
			if(typeof document.documentElement.style.opacity!='undefined'){
				$(this).animate({opacity: socialInactiveAlpha});
			}
		  }
		);
	});
	
	//Enable Tabs
	$("ul.tabs2menu").tabs("div.panels > div", {tabs:'li'});
	
	//ADD TOGGLE CONTENT FUNCTIONALITY
	$('.toggle').click(function() {
		$(this).siblings('.toggle_show').slideToggle('fast');
		if($(this).children().hasClass('up')){
			$(this).children().removeClass('up');
			$(this).children().addClass('down');
			$(this).parent('.toggleWrapper').removeClass('inactive');
			$(this).parent('.toggleWrapper').addClass('active');
		}
		else if($(this).children().hasClass('down')){
			$(this).children().removeClass('down');
			$(this).children().addClass('up');
			$(this).parent('.toggleWrapper').removeClass('active');
			$(this).parent('.toggleWrapper').addClass('inactive');
		}
	});
	
	//ADD SEARCH INPUT ANIMATION
	$('#search_field').focus(function() {
		$(this).fadeTo('fast', 1);
	});
	$('#search_field').blur(function() {
		$(this).fadeTo('fast', 0);
	});
	
	$('#headerSearchField').focus(function() {
		$(this).fadeTo('fast', 1);
	});
	$('#headerSearchField').blur(function() {
		$(this).fadeTo('fast', 0);
	});

	$('#searchsubmit').val('');
	$('#s').focus(function() {
		$(this).fadeTo('fast', 1);
	});
	$('#s').blur(function() {
		$(this).fadeTo('fast', 0);
	});
	$("#s").click(function() {
		this.value = '';
	});
	
	
	//Preload Images
	$('.imageWrapper img').imgpreload
	({
		each: function()
		{
			if($(this).siblings().length > 0){
				$(this).siblings('.imagePreloader').delay(700).fadeOut('slow');
			}
			else{
				$(this).parent().siblings('.imagePreloader').delay(700).fadeOut('slow');
			}
		},
		all: function()
		{
		}
	});
	
	//hide preloaders on hidden images
	if ($('.imagePreloader:hidden').length ) {
		$('.imagePreloader:hidden').css('display','none');
	}
	if ($('.kwicksPreloader:hidden').length ) {
		$('.kwicksPreloader:hidden').css('display','none');
	}
	if ($('.nivoPreloader:hidden').length ) {
		$('.nivoPreloader:hidden').css('display','none');
	}
	
	//ADD IMAGE ICON HOVER LISTENERS/HANDLERS
	$('.iconHolder').each(function(index) {
		var prt = $(this).parents('.imageWrapper');
		prt.hover(
		  function () {
			$(this).find('.responsiveImage').stop().animate({ opacity: 0.5 }, 300, 'easeOutExpo');
			$(this).find('.iconHolder').animate({ opacity: 1, left: '0', top: '0' }, 300, 'easeOutExpo');
		  }, 
		  function () {
			$(this).find('.responsiveImage').stop().animate({ opacity: 1 }, 300, 'easeInExpo');
			$(this).find('.iconHolder').animate({ opacity: 0, left: '150%', top: '150%'}, 300, 'easeInExpo', function(){
				$(this).css({left: '-150%', top: '-150%'});
			});
		
		  }
		);
	});
	
	//Remove bottom margin from last widget
	if(jQuery('#sideBarWidgets').length){
		jQuery('#sideBarWidgets').children('.widget:last').css({'margin-bottom':'0px','padding-bottom':'0px','border-bottom':'none'});
	}
	//Remove bottom margin from last tweet
		window.setTimeout(function(){
			$('.tweet_list').each(function(index) {
				jQuery(this).children('.item:last').css({'margin-bottom':'0px'});
			});
		}, 2000);
	
	//ADD SCROLL TO TOP ANIMATION
    $(".backToTop").click(function(event){
        event.preventDefault();
        //goto that anchor by setting the body scroll top to anchor top
        $('html, body').animate({scrollTop:0}, 500);
    });
	
	//ADD BUTTON STYLES TO WP GENERATED HTML
	$('.comment-reply-link').addClass('button tiny '+ defaultBtnColor);
	$('#submit').addClass('button medium '+ defaultBtnColor);
	$('#cancel-comment-reply-link').addClass('buttonPro '+ defaultBtnColor);
	

	//ADD COLORBOX FUNCTIONALITY FOR IMAGES
	$('.lightbox[href*="http://vimeo.com/"]').each(function(){
		$(this).attr('href', this.href.replace("vimeo.com/", "player.vimeo.com/video/"));
	});
	$('.lightbox[href*="http://www.vimeo.com/"]').each(function(){
		$(this).attr('href', this.href.replace("www.vimeo.com/", "player.vimeo.com/video/"));
	});
	
	//Clean Up Youtube Url's
	var regex1 = new RegExp('feature=player_embedded&', 'i');
	var regex2 = new RegExp('watch\\?v=', 'i');
	$('.lightbox[href*="http://www.youtube.com/"]').each(function() {
		$(this).attr('href',this.href.replace(regex1,''));
	});
	$('.lightbox[href*="http://www.youtube.com/"]').each(function() {
		$(this).attr('href',this.href.replace(regex2,'v/'));
	});
	
	$('.lightbox').each(function(index) {
		//remove button classes & then add them back in at end
		var btnClasses = '';
		if ($(this).attr('data-btn')){
			btnClasses = $(this).attr('data-btn');
			$(this).removeClass(btnClasses);
		}
		$(this).removeClass('lightbox');
		var vWidth;
		var vHeight;
		var groupName = '';
		var relObj;
		if($(this).attr('class') == 'lbIFrame'){
			vWidth = $(this).attr('data-iframewidth');
			vHeight = $(this).attr('data-iframeheight');
			$(this).colorbox({width:vWidth, height:vHeight, iframe:true});
		}
		else if($(this).attr('class') == 'lbVideo'){
			vWidth = $(this).attr('data-iframewidth');
			vHeight = $(this).attr('data-iframeheight');
			$(this).colorbox({iframe:true, innerWidth:vWidth, innerHeight:vHeight});
		}
		else{
			if ($(this).attr('data-rel')){
				groupName = $(this).attr('data-rel');
				relObj = {rel:groupName}
			}
			$(this).colorbox(relObj); 
		}
		
		if ($(this).attr('data-btn')){
			$(this).addClass(btnClasses);
		}
		
	});
	
	addToolTips();
	//Disable Social Tooltips on Mobile and Tablets
	var bWidth = $(window).width();
	if(bWidth < 990){
		$('.vtip').each(function(index) {
			$(this).removeClass('vtip');
			$(this).addClass('ttip');
			$(this).unbind();
		});
	}
	//Re-Enable or Disable Social ToolTips on Resize
	$(window).resize(function() {
		bWidth = $(window).width();
		if(bWidth < 990){
			$('.vtip').each(function(index) {
				$(this).removeClass('vtip');
				$(this).addClass('ttip');
				$(this).unbind();
			});
		}
		else{
			if ($(".ttip").length > 0){
				$('.ttip').each(function(index) {
					$(this).removeClass('ttip');
					$(this).addClass('vtip');
				});
				addToolTips();
			}
		}
	});
	
	$(function(){
		
		var $portfolioGrid = $('#portfolioGrid');

		$portfolioGrid.imagesLoaded( function(){
		  $portfolioGrid.isotope({
			itemSelector : '.element',
			resizable : true,
			resizesContainer : true,
			containerStyle : { position: 'relative', overflow: 'hidden' },
			transformsEnabled : true,
			layoutMode : 'fitRows'
		  });
		});
			    
		var $optionSets = $('#options .option-set'),
			$optionLinks = $optionSets.find('a');
		
		//PORTFOLIO CATEGORY CLICK HANDLER
		$optionLinks.click(function(){
		
			var $this = $(this);
			if ( $this.hasClass('selected') ) {
				return false;
			}
			
			var $optionSet = $this.parents('.option-set');
			$optionSet.find('.selected').removeClass('selected');
			$this.addClass('selected');

			// make option object dynamically, i.e. { filter: '.my-filter-class' }
			var options = {},
				key = $optionSet.attr('data-option-key'),
				value = $this.attr('data-option-value');
				
			value = value === 'false' ? false : value;
			options[ key ] = value;
			
			if ( key === 'layoutMode' && typeof changeLayoutMode === 'function' ) {
				// changes in layout modes need extra logic
				changeLayoutMode( $this, options )
			} 
			else {
				// otherwise, apply new options
				$portfolioGrid.isotope( options );
			}
			
			return false;
		});

    });
	
	
});

function addToolTips(){
	/**
	Vertigo Tip by www.vertigo-project.com
	*/
	this.vtip = function() {    
		this.xOffset = -25; // x distance from mouse
		this.yOffset = -40; // y distance from mouse       
		
		jQuery(".vtip").unbind().hover(    
			function(e) {
				this.t = this.title;
				this.title = ''; 
				this.top = (e.pageY + yOffset); this.left = (e.pageX + xOffset);
				
				jQuery('body').append( '<div id="vtip" style="z-index:30000;">' + this.t + '<div class="vTipArrow"></div></div>' );
						
				jQuery('div#vtip').css("top", this.top+"px").css("left", this.left+"px").fadeIn("fast");
				
			},
			function() {
				this.title = this.t;
				jQuery("div#vtip").fadeOut("fast").remove();
			}
		).mousemove(
			function(e) {
				this.top = (e.pageY + yOffset);
				this.left = (e.pageX + xOffset);
							 
				jQuery("div#vtip").css("top", this.top+"px").css("left", this.left+"px");
			}
		);
	};
	jQuery(document).ready(function(jQuery){vtip();})
}

function uniqeid(){
	var newDate = new Date;
	return newDate.getTime();
}

/*
 * Fix for Google Chrome on Android where the fixed positioning of background elements causes the backgrounds to overlap the rest of the content
 */
(function(){
	var lowercase_useragent = navigator.userAgent.toLowerCase()
	if(/chrome/.test(lowercase_useragent) && /android/.test(lowercase_useragent)){
		var $ = jQuery;
		$(document).ready(function(){
			var backgroundImage = $('#backgroundImage'),
				backgroundPattern = $('#backgroundPattern'),
				body = $('body'),
				css_corrections = {
					position: 'absolute'
				};
			
			backgroundImage.css(css_corrections);
			backgroundPattern.css(css_corrections);
			
			function correct_height(){
				backgroundImage.height(0);
				backgroundPattern.height(0);
				var height = body.height();
				backgroundImage.height(height);
				backgroundPattern.height(height);
			}
			window.addEventListener('resize',correct_height);
			correct_height();
		});
	}
})();