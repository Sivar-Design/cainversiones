jQuery.noConflict();
function setupFlex(arrayID){
	jQuery(document).ready(function($) {
		var uniqueDivId = "#" + arrayID['uniqueID'];
		var flexSlider = uniqueDivId + ' .flexslider';
		$(flexSlider).flexslider(arrayID);
	});
}