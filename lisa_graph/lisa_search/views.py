from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, redirect
from lisa_search.forms import UploadDataForm
from lisa_modules.csv_reader import CSV
from lisa_models.table import Table_Model
from lisa_modules.db_middleware import persist_csv, get_last_created_tables, filter_tables
from lisa_modules.key_middleware import get_all_keys
from mongoengine import connect
import tempfile

# Create your views here.
def index(request):
    return render_to_response(
        'index.html', 
        {}, 
        context_instance=RequestContext(request)
    )

def search(request):
    last_tables = get_last_created_tables()
    keys = get_all_keys()
    if request.method == 'POST': # If the form has been submitted...
        # ContactForm was defined in the previous section
        #import pudb; pudb.set_trace()
        keys_selected = request.POST.getlist('filterlist') or None
        filtered_entries = filter_tables(keys_selected)
        return render_to_response(
            'lisa_search/search.html', 
            {'selected_keys': keys_selected,'keys': keys,
                'filtered_entries': filtered_entries}, 
            context_instance=RequestContext(request)
        )
    else:
        return render_to_response(
            'lisa_search/search.html', 
            {'last_entries': last_tables, 'keys': keys}, 
            context_instance=RequestContext(request)
        )

def upload(request):
    if request.method == 'POST': # If the form has been submitted...
        # ContactForm was defined in the previous section
        if request.FILES:
            form = UploadDataForm(request.POST, request.FILES) # A form bound to the POST data
        else:
            form = UploadDataForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            data = request.FILES['data_set_file'].read()
            my_f = tempfile.NamedTemporaryFile(delete=False)
            my_f.file.write(data)
            my_f.close()
            connect('lisa_project_db')
            list_key = None
            csv_object = CSV()
            csv_object.initialize(my_f.name, 
                                form.data['name'], 
                                form.data['description'])
            persist_csv(csv_object, list_key)
            
            return render_to_response(
                'lisa_search/upload.html', 
                {}, 
                context_instance=RequestContext(request))
    else:
        form = UploadDataForm() # An unbound form

    return render_to_response(
        'lisa_search/upload.html', 
        {'form':form}, 
        context_instance=RequestContext(request))

def show_table(request, table_name):
    last_tables = get_last_created_tables()
    keys = get_all_keys()
    if request.method == 'POST': # If the form has been submitted...
        # ContactForm was defined in the previous section
        #import pudb; pudb.set_trace()
        keys_selected = request.POST.getlist('filterlist') or None
        filtered_entries = filter_tables(keys_selected)
        return render_to_response(
            'lisa_search/search.html', 
            {'selected_keys': keys_selected,'keys': keys,
                'filtered_entries': filtered_entries}, 
            context_instance=RequestContext(request)
        )
    else:
        return render_to_response(
            'lisa_search/search.html', 
            {'last_entries': last_tables, 'keys': keys}, 
            context_instance=RequestContext(request)
        )

