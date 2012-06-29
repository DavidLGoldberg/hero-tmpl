(function($){
    //There's a better namespaced way to do this...
    $.fn.htSection_payloadBaseUrl = "/api";
    $.fn.htSection_templateBaseUrl = "/templates";

    $.fn.htSection = function(options) {

        var settings = $.extend( {

        }, options);

        return this.each(function() {
            var $this = $(this);

            var payloadBaseUrl = settings.payloadBaseUrl || $this.data('payload-base-url') ||  $.fn.htSection_payloadBaseUrl || '';
            var templateBaseUrl = settings.templateBaseUrl || $this.data('template-base-url') || $.fn.htSection_templateBaseUrl || '';

            var payloadAction = settings.payloadAction || $this.data('payload-action');
            var templateName = settings.templateName || $this.data('template-name');

            templateName = templateName || payloadAction;

            $.ajax({
                url: templateBaseUrl + templateName,
                type: 'GET',
                cache: false,
                success: function(template) {
                    var tmpl = Hogan.compile(template);

                    $.ajax({
                        url: payloadBaseUrl + payloadAction,
                        type: 'GET',
                        cache: false,
                        dataType: 'json',
                        success: function(payload) {
                            $this.html(tmpl.render(payload));
                        }
                    });
                }
            });
        }); //end: each

    }; //end: init
})(jQuery);
