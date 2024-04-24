import json
from hashlib import md5


def gen_edu(data: list[dict]) -> str:
    return '\n'.join(f'''
<div id="{item["Degree"]}" class="mb-4 ms-4">
    <div class="small text-secondary">
        <i class="bi bi-calendar3"></i>
        {item["Time"]}
    </div>
    <h3 class="text-body fs-4 mb-1">
        {item["Institution"]}
    </h3>
    <div>
        {item["Degree"]} of {item["Major"]} in {item["Discipline"]}
    </div>
</div>
    ''' for item in data)


def gen_pub(data: list[dict]) -> str:
    retval = ''
    for item in data:
        id = md5(item['Title'].encode()).hexdigest()
        with open(item['Bibtex'], 'r') as f:
            bib = f.read()
        retval += f'''
<div id="{id}" class="mb-4 ms-4">
    <div class="small text-secondary">
        <i class="bi bi-calendar3"></i>
        {item["Time"]} /
        <a data-bs-toggle="modal" data-bs-target="#{id}-Modal" href="#" class="text-primary-emphasis">
            <i class="bi bi-quote"></i>
            Cite
        </a>
        /
        <a href="{item["Link"]}" class="text-primary-emphasis">
            <i class="bi bi-three-dots"></i>
            Details
        </a>
    </div>
    <h3 class="text-body fs-4 mb-1">
        {item["Title"]}
    </h3>
    <div>
        <i>{item["Source"]}</i>
    </div>
    <h4 class="text-body fs-5 mt-2 mb-0">
        Authors
    </h4>
    <div>{item["Authors"]}</div>
    <div id="{id}-Modal" class="modal fade">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title text-body fs-5" id="exampleModalLabel">BibTex</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <pre id="{id}-Cite" class="code overflow-x-scroll card card-body">{bib}</pre>
                </div>
            </div>
        </div>
    </div>
</div>
        '''
    return retval


def gen_exp(data: list[dict]) -> str:
    return '\n'.join(f'''
<div id="steganography" class="mb-4 ms-4">
    <div class="small text-secondary">
        <i class="bi bi-calendar3"></i>
        {item["Time"]} {'/ <i class="bi bi-hourglass-split"></i> under research' if not item.get("Finished", True) else ''}
    </div>
    <h3 class="text-body fs-4 mb-1">{item["Subject"]}</h3>
    <div><i>{item["Type"]}</i></div>
    <h4 class="text-body fs-5 mt-2 mb-0">
        Introduction
    </h4>
    <div>{item["Introduction"]}</div>
    <h4 class="text-body fs-5 mt-2 mb-0">
        Contributions
    </h4>
    <div>{item["Contributions"]}</div>
    <h4 class="text-body fs-5 mt-2 mb-0">
        Supervisor
    </h4>
    <div>{item["Supervisor"]}</div>
</div>
    ''' for item in data)


def gen_doc(data: dict, dark_theme: bool=False) -> str:
    return f'''
<!DOCTYPE html>
<html lang="en"{' data-bs-theme="dark"' if dark_theme else ''}>

<head>
    <meta charset="UTF-8">
    <meta name="author" content="Jinyi Xia">
    <meta name="description" content="Homepage of Jinyi Xia">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
    <title>Jinyi Xia's Homepage</title>
    <link rel="icon" type="image/png" href="imgs/favicon.png">
    <script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm"
        crossorigin="anonymous"></script>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">
    <link href="style.css" rel="stylesheet">
    <base target="_blank">
</head>

<body>
    <div class="container-fluid bg-body-tertiary">
        <nav class="navbar navbar navbar-expand-sm">
            <div class="container">
                <a class="navbar-brand text-primary-emphasis" href="#top" target="_self">About Me</a>
                <div>
                    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
                        aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                        <i class="bi bi-list"></i>
                    </button>
                </div>
                <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav">
                        <li class="nav-item">
                            <a class="nav-link" aria-current="page" href="#education" target="_self">Education</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" aria-current="page" href="#publications" target="_self">Publications</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" aria-current="page" href="#experiences" target="_self">Experiences</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    </div>
    <div class="container mb-3 text-body-secondary">
        <div id="introduction-mobile" class="row mt-3">
            <div class="col-auto">
                <img id="photo" decoding="async" src="{data["Introduction"]["Avatar"]}" class="rounded-circle" alt="Jinyi Xia"
                    style="height: 64px">
            </div>
            <div class="col">
                <div class="fs-5 text-primary-emphasis">
                    {data["Introduction"]["Name"]} <span class="fs-6 text-body"> {data["Introduction"]["Name-cn"]} </span>
                </div>
                <div>
                    {data["Introduction"]["Brief"]}
                </div>
            </div>
            <div class="col-auto">
                <a href="#" target="_self" class="fs-4 me-2 text-primary-emphasis" style="text-decoration: none;" data-bs-toggle="tooltip"
                    data-bs-placement="bottom" data-bs-title="{data["Introduction"]["Location"]}">
                    <i class="bi bi-geo-alt-fill"></i>
                </a>
                <a href="#" target="_self" class="fs-4 me-2 text-primary-emphasis" style="text-decoration: none;" data-bs-toggle="tooltip"
                    data-bs-placement="bottom" data-bs-title="{data["Introduction"]["Institution"]}">
                    <i class="bi bi-building-fill"></i>
                </a>
                <a href="mailto:{data["Introduction"]["Email"]}" class="fs-4 me-2 text-primary-emphasis" style="text-decoration: none;" data-bs-toggle="tooltip" data-bs-placement="bottom" data-bs-title="{data["Introduction"]["Email"]}">
                    <i class="bi bi-envelope-fill"></i>
                </a>
                <a href="https://github.com/{data["Introduction"]["Github"]}" class="fs-4 me-2 text-primary-emphasis" style="text-decoration: none;" data-bs-toggle="tooltip" data-bs-placement="bottom" data-bs-title="{data["Introduction"]["Github"]}">
                    <i class="bi bi-github"></i>
                </a>
            </div>
        </div>
        <div class="row">
            <div id="introduction-full" class="col-lg-3 mt-3">
                <img id="photo" decoding="async" src="{data["Introduction"]["Avatar"]}" class="rounded-circle" alt="{data["Introduction"]["Name"]}"
                    style="width: 60%; max-width: 150px; min-width: 128px;">

                <h1 id="name" class="mt-3 mb-4">
                    <div class="fs-3 text-primary-emphasis">
                        {data["Introduction"]["Name"]}
                    </div>
                    <div class="fs-5 text-body">
                        {data["Introduction"]["Name-cn"]}
                    </div>
                </h1>

                <div id="contact" class="mt-4">
                    <p id="brief">
                        {data["Introduction"]["Brief"]}
                    </p>
                    <p id="city">
                        <i class="bi bi-geo-alt-fill"></i>
                        {data["Introduction"]["Location"]}
                    </p>
                    <p id="institute">
                        <i class="bi bi-building-fill"></i>
                        {data["Introduction"]["Institution"]}
                    </p>
                    <p id="email">
                        <i class="bi bi-envelope-fill"></i>
                        <a href="mailto:{data["Introduction"]["Email"]}" class="text-body-secondary">
                            {data["Introduction"]["Email"]}
                            <i class="bi bi-link-45deg"></i>
                        </a>
                    </p>
                    <p id="github">
                        <i class="bi bi-github"></i>
                        <a href="https://github.com/XIA-Jinyi" class="text-body-secondary">
                            {data["Introduction"]["Github"]}
                            <i class="bi bi-link-45deg"></i>
                        </a>
                    </p>
                </div>
            </div>

            <div id="portfolio" class="col-lg-9">
                <div id="education">
                    <h2 class="text-primary-emphasis mt-4 mb-3" style="font-variant:small-caps">
                        <i class="bi bi-mortarboard"></i>
                        Education
                    </h2>

                    {gen_edu(data["Education"])}
                </div>

                <div id="publications">
                    <h2 class="mt-4 mb-3 text-primary-emphasis" style="font-variant:small-caps">
                        <i class="bi bi-newspaper"></i>
                        Publications
                    </h2>

                    {gen_pub(data["Publications"])}
                </div>

                <div id="experiences">
                    <h2 class="mt-4 mb-3 text-primary-emphasis" style="font-variant:small-caps">
                        <i class="bi bi-people"></i>
                        Experiences
                    </h2>

                    {gen_exp(data["Experiences"])}
                </div>
            </div>
        </div>
    </div>
    <div class="container-fluid bg-body-tertiary">
        <div class="container">
            <div class="row text-secondary small">
                <div style="height: 2em;">
                </div>
                <div>
                    @ 2023 Jinyi Xia.
                    <br>
                    Powered by <a href="https://getbootstrap.com/" class="text-secondary"><i class="bi bi-bootstrap-fill"></i> Bootstrap</a> & <a href="https://github.com/" class="text-secondary"><i class="bi bi-github"></i> GitHub</a>.
                    <br>
                    Licensed under <a href="https://github.com/XIA-Jinyi/XIA-Jinyi.github.io/blob/main/LICENSE" class="text-secondary">MIT License</a>.
                </div>
                <div style="height: 2em;">
                </div>
            </div>
        </div>
    </div>
</body>
'''+\
'''
<script>
    // 初始化提示框
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl)
    })

    function updateTheme() {
        const theme = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
        document.documentElement.setAttribute('data-bs-theme', theme);
    }

    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', updateTheme);
    updateTheme(); 
</script>

</html>
'''


if __name__ == '__main__':
    with open('info.json', 'r') as f:
        data = json.load(f)
    print(gen_doc(data))