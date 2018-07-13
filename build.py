from staticjinja import make_site

if __name__ == "__main__":
    context = {'knights': ['sir arthur', 'sir lancelot', 'sir galahad']}
    site = make_site(contexts=[('index.html', context)], outpath='./static/')
    site.render()