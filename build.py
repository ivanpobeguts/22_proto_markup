from staticjinja import make_site


def render_pages():
    context = {'username': 'Леонид Федорович',
               'STATIC_URL': '../static'}
    site = make_site(
        contexts=[('index.html', context),
                  ('apps_page.html', context)],
        outpath='./static/')
    site.render()


if __name__ == '__main__':
    render_pages()
