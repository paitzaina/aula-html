from django.shortcuts import render

# Create your views here.
def curriculo_spiff(request):
    '''
    View function for the astronaut Spiff's resume page.
    Renders the spiff.html template.
    This will display the resume page when the corresponding URL is accessed
    The curriculo_spiff view is responsible for displaying the content of the resume page
    It is a simple function-based view
    It takes a request object as a parameter
    It returns a rendered HTML response
    @param request: The HTTP request object
    @return: Rendered HTML response with resume page content
    '''
    return render(request, 'curriculo/spiff.html')