import json
from staticjinja import make_site


def load_data(filepath):
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)


def pretty_print_json(data):
    print(json.dumps(data, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    applications = load_data('./templates/json/applications.json')
    index_context = {'last_applications': applications[:5]}
    applications_page1_context = {'applications': applications[:5]}
    applications_page2_context = {'applications': applications[5:10]}

    site = make_site(
        searchpath='templates',
        outpath='site',
        contexts=[
            ('index.html', index_context),
            ('pages/applications_p1.html', applications_page1_context),
            ('pages/applications_p2.html', applications_page2_context)
        ]
    )
    site.render(use_reloader=True)
