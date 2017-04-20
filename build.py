import json
from staticjinja import make_site


def load_data(filepath):
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)


def get_contexts():
    app_pages_iter = get_applications_page()
    last_applications = next(app_pages_iter)
    index_context = {
        'static': get_static(),
        'last_applications': last_applications
    }
    applications_page1_context = {
        'static': get_static(),
        'applications': last_applications
    }
    applications_page2_context = {
        'static': get_static(),
        'applications': next(app_pages_iter)
    }
    account_context = catalogue_context = company_context = concrete_goods_context = {
        'static': get_static()
    }
    contexts = [
        ('index.html', index_context),
        ('account.html', account_context),
        ('applications_page1.html', applications_page1_context),
        ('applications_page2.html', applications_page2_context),
        ('catalogue.html', catalogue_context),
        ('company.html', company_context),
        ('concrete_goods.html', concrete_goods_context)
    ]

    return contexts


def get_static():
    return {
        'css': {
            'bootstrap': 'css/bootstrap.min.css',
            'jumbotron': 'css/jumbotron-narrow.css',
            'style': 'css/style.css'
        },
        'js': {
            'jquery': 'js/jquery-3.1.1.min.js',
            'bootstrap': 'js/bootstrap.min.js'
        },
        'img': {
            'favicon': 'img/favicon.ico',
            'logo': 'img/logo.png'
        }
    }


def get_applications_page():
    applications_json_dir = './templates/_json/applications.json'
    applications = load_data(applications_json_dir)
    app_page_count = 5
    for pos in range(0, len(applications), app_page_count):
        yield applications[pos: pos + app_page_count]


if __name__ == "__main__":
    site = make_site(
        searchpath='templates',
        outpath='site',
        contexts=get_contexts()
    )
    site.render(use_reloader=True)
