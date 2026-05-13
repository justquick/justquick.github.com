"""
Pelican plugin that provides site data to Jinja2 templates as SITEDATA.
"""

from pelican import signals


INFO = {
    "email": "justquick@gmail.com",
    "location": "Washington, DC",
    "phone": "410.941.9553",
    "title": "Software Developer and Technologist",
    "mission": (
        "I build and contribute to open-source technologies that power organizations"
        " and communities worldwide. My work spans scalable web applications, developer"
        " tooling, and cloud infrastructure—with a focus on meaningful impact and engineering excellence."
    ),
    "social": {
        "github-square": "justquick",
        "linkedin-square": "justquick",
    },
    "skills": {
        "Linux Sys Admin": 20,
        "Python & Django": 20,
        "SQL": 19,
        "APIs/Integrations": 17,
        "JavaScript": 17,
        "Agile": 16,
        "DevOps": 15,
        "Cloud/AWS": 11,
        "BI Analytics/Data Science": 7,
    },
}

WORKS = [
    {
        "company": "C4ADS",
        "link": "https://c4ads.org",
        "position": "Head of Software",
        "dates": "Aug 2025 - Present",
        "duties": [
            "Lead the engineering team building a SaaS platform for investigating illicit networks and financial crime.",
        ],
    },
    {
        "company": "OttLaw LLC",
        "link": "https://ottlaw.com",
        "position": "Webmaster",
        "dates": "Sept 2024 - Present",
        "duties": [
            "Redesigned the firm's website from a single-page Squarespace site to a multi-page WordPress site with a custom-built theme.",
            "Integrated click-to-call, XML sitemaps, contact forms, social media feeds, Google Analytics, and Google Business reviews.",
            "Designed and implemented a comprehensive SEO, performance, and caching strategy, improving PageSpeed scores from a C to an A.",
            "Set up and managed Google and Facebook advertising campaigns.",
            "Trained staff on WordPress and all integrated third-party services.",
        ],
    },
    {
        "company": "NASA Space Telescope Science Institute",
        "link": "https://www.stsci.edu",
        "position": "Principal IT Technologist",
        "dates": "Aug 2019 - Apr 2024",
        "duties": [
            "Developed CI/CD pipelines using GitLab, Docker, and Kubernetes to deploy vendor and in-house applications to AWS and on-premises cloud environments.",
            "Built a system performance reporting platform using Python, PostgreSQL, Django REST Framework, and Tableau, aggregating KPIs from GitLab, Jira, Confluence, Slack, Box, Cisco UC, and others; later migrated high-priority endpoints to a FastAPI service backed by Neo4j and ClickHouse.",
            "Served as technical lead for the Science Mission Office's Hubble library archive, built on Lucidea's ArchivEra LMS; gathered stakeholder requirements, evaluated solutions, and drove implementation.",
            "Designed a scalable cloud rendering environment for Houdini 3D clients using VMware, Kubernetes, and Terraform.",
            "Founding member of the cross-divisional Private Cloud Engineering Team, establishing best practices for deploying applications across multi-cloud environments.",
            "Led the FedRAMP/ITAR-compliant rollout of Box using AWS KMS for encryption key management.",
        ],
    },
    {
        "company": "Gnarwhal Studios, INC.",
        "link": "https://web.archive.org/web/20200609073941/http://gnarwhalstudios.com/",
        "position": "CTO and Application Developer",
        "dates": "2005 - 2021",
        "duties": [
            "Oversaw all technical decisions for Gnarwhal Studios' production websites and the Humans vs. Zombies game platform.",
            "Led architecture and development of the HvZ game-tracking web application in Python and Django.",
            'Products included <a href="http://humansvszombies.org">Humans vs. Zombies</a> and <a href="http://slap45.com">Slap 45</a>.',
        ],
    },
    {
        "company": "REW Consulting Services",
        "position": "Senior Software Engineer",
        "dates": "Oct 2018 - May 2019",
        "duties": [
            "Embedded with a Fortune 50 financial services firm.",
            "Built a web application on top of Puppet to orchestrate software deployments across the enterprise.",
            "Designed SOA micro-service controllers to push updates across approximately 80,000 nodes.",
            "Built a search service combining Python, Elasticsearch, Puppet facts, and application metadata.",
        ],
    },
    {
        "company": "Anthem Engineering, LLC",
        "position": "Senior Application Developer",
        "dates": "October 2017 - April 2018",
        "duties": [
            "Integrated the Box.com API as the document storage backend.",
            "Built a real-time communications layer using Redis, PostgreSQL, and django-channels to push model updates to clients via WebSockets.",
            "Diagnosed and resolved Ruby/Sinatra defects while onboarding to the language.",
        ],
    },
    {
        "company": "b.well Connected Health",
        "position": "Senior Engineer",
        "dates": "September 2016 - November 2016",
        "duties": [
            "Integrated proprietary health insurance databases into MySQL to track coverage details including copays, deductibles, and out-of-pocket limits.",
            "Normalized lab result tracking across varying test and reference ranges using PostgreSQL and Django REST Framework to deliver data to a mobile application.",
            "Integrated Stripe to handle recurring monthly subscription billing.",
        ],
    },
    {
        "company": "National Geographic Society",
        "link": "https://www.nationalgeographic.com",
        "position": "Senior Application Developer",
        "dates": "April 2013 - July 2016",
        "duties": [
            "Led backend development of the digital magazine platform, delivering a PostgreSQL/Django API consumed by a third-party mobile application.",
            "Implemented CI/CD pipelines using Jenkins and Linux containers across all Python-powered web properties.",
            "Contributed to the services team on internal API workflow management and SOA application initiatives.",
            'Served as technical lead for <a href="https://yourshot.nationalgeographic.com/">Your Shot</a>, National Geographic\'s global photo-sharing community.',
        ],
    },
    {
        "company": "SocialToaster Inc",
        "position": "Senior Application Developer",
        "dates": "September 2012 - February 2013",
        "duties": [
            "Engaged as a PostgreSQL and Django consultant to gamify social content amplification for brand clients.",
            "Introduced CI/CD pipelines, testing standards, and documentation practices to the engineering team.",
            "Extended platform integrations to additional social networks, including YouTube, via Python.",
        ],
    },
    {
        "company": "Bolster Labs Inc. AKA Chalk and Chisel",
        "position": "Senior Application Developer",
        "dates": "December 2012",
        "duties": [
            "Integrated Kentico CMS with Facebook Pages for livestrong.org.",
            'Enhanced fragileoasis.org (NASA) with activity streams powered by <a href="https://django-activity-stream.readthedocs.io/en/latest/">django-activity-stream</a>, my open-source project.',
            "Built a contest judging interface within Django Admin for National Geographic photography competitions.",
        ],
    },
    {
        "company": "National Geographic Society",
        "link": "https://www.nationalgeographic.com",
        "position": "Application Developer",
        "dates": "December 2010 - December 2012",
        "duties": [
            "Developed features on a shared PostgreSQL and Django CMS powering National Geographic's newsroom content production.",
            'Built a photo contest submission platform for <a href="https://www.nationalgeographic.com/travel/contests/travel-photo-contest-2019/">NatGeo Travel and Kids</a>.',
        ],
    },
    {
        "company": "Lifemax Inc.",
        "position": "Django Developer",
        "dates": "June 2009 - June 2010",
        "duties": [
            "Extended the PostgreSQL and Django application to support internationalization, enabling staff to author and manage multilingual content.",
            "Migrated the full application stack to Media Temple hosting.",
            "Optimized page load performance and media asset delivery.",
        ],
    },
    {
        "company": "The Washington Times",
        "link": "https://www.washingtontimes.com",
        "position": "Web Developer",
        "dates": "Dec 2008 - June 2010",
        "duties": [
            "Administered the Ellington CMS (the precursor to open-source Django).",
            "Served as PostgreSQL DBA.",
            "Developed Python/Django applications with a focus on scalability and performance.",
            'Open-sourced several internal projects, most available through <a href="https://github.com/callowayproject/Calloway">The Calloway Project</a>.',
        ],
    },
    {
        "company": "Open Source Connections",
        "position": "Web Application Developer",
        "dates": "Jan 2008 - Mar 2008",
        "duties": [
            "Developed Django applications for a work-order workflow management system.",
            "Built AJAX utilities including a full CRUD interface.",
            "Provided post-deployment debugging and end-user support.",
        ],
    },
    {
        "company": "Go MCN AKA Live Networks Corp.",
        "position": "Developer & MySQL Administrator",
        "dates": "2007",
        "duties": [
            "Built a physician directory website and implemented initial audio telemedicine capabilities.",
            "Managed MySQL on a VPS, handling user administration and capacity planning.",
        ],
    },
    {
        "company": "Groupus / Firefeeds",
        "position": "Developer & Fedora Administrator",
        "dates": "2006",
        "duties": [
            "Configured the GroupUS social networking platform with a focus on real-time audio communication.",
            "Deployed PBX software to broadcast local Washington, D.C. fire and police communications.",
            "Built a Django-powered community networking site.",
        ],
    },
    {
        "company": "Humans vs Zombies Inc.",
        "link": "https://web.archive.org/web/20200609073918/https://humansvszombies.org/",
        "position": "Web Developer / Ubuntu Administrator",
        "dates": "2006",
        "duties": [
            "Created HvZSource, a web platform managing game hosting across six continents.",
            "Built a custom Django application to track game events, players, tags, and kills.",
            "Managed mass email campaigns via SendGrid.",
        ],
    },
]


def load_data(generator):
    skill_list = [
        {"name": name, "years": years, "percent": min(years * 5, 100)}
        for name, years in INFO["skills"].items()
    ]
    generator.context["SITEDATA"] = {
        "info": {**INFO, "skill_list": skill_list},
        "works": WORKS,
    }


def register():
    signals.generator_init.connect(load_data)
