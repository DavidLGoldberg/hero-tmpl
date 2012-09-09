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

            $.when(
                $.ajax({
                    url: payloadBaseUrl + payloadAction,
                    type: 'GET',
                    dataType: 'json'}),
                $.ajax({
                    url: templateBaseUrl + templateName,
                    type: 'GET'}))
            .done(function(payload, template) {
                var tmpl = Hogan.compile(template[0]);
                $this.html(tmpl.render(payload[0]));
            });
        }); //end: each

    }; //end: init
})(jQuery);
