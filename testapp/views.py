from django.views.generic import ListView, TemplateView


class JsTest(TemplateView):
    template_name = "testapp/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'test_text':'This is Django test text!',
        })
        return context



