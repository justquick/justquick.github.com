# Justin Quick GitHub Pages - Pelican Static Site

This site is built using [Pelican](https://getpelican.com/), a Python static site generator that uses Jinja2 templates and Markdown for content authoring.

## Project Structure

```
/
├── content/              # Static assets (CSS, JS, images, favicons)
├── markdown-content/     # Markdown source files for pages
│   └── pages/           # Page content (resume.md, pe.md, etc.)
├── themes/justquick/    # Custom Pelican theme
│   ├── templates/       # Jinja2 templates
│   │   ├── index.html   # Homepage template
│   │   ├── page-resume.html  # Resume page template
│   │   └── page-pe.html      # Professional experience template
│   └── static/          # Theme-specific assets
├── pelican-plugins/     # Custom Pelican plugins
│   └── yaml_loader.py   # Loads YAML data into templates
├── info.yaml            # Personal information data
├── work.yaml            # Work experience data
├── pelicanconf.py       # Pelican development configuration
├── publishconf.py       # Pelican production configuration
├── requirements.txt     # Python dependencies
├── templates/           # Legacy templates (kept for reference)
├── .github/workflows/   # GitHub Actions CI/CD
│   └── build.yml        # Build and deploy workflow
└── [legacy directories] # Old project docs (preserved as-is)
    ├── django-activity-stream/
    ├── google-chartwrapper-apidoc/
    ├── jeebusisgod/
    └── ...
```

## Content Management

### Adding or Editing Pages

1. **Create/edit markdown files** in `markdown-content/pages/`:
   ```markdown
   Title: Page Title
   Template: page-resume  # Optional: use custom template
   Status: published
   Slug: my-page         # URL will be /my-page.html

   Your markdown content here...
   ```

2. **Available templates**:
   - `page-resume` - Full resume layout with sidebar
   - `page-pe` - Simple professional experience list
   - Default `page` template for basic pages

### Updating Personal Info

Edit `info.yaml`:
```yaml
email: your@email.com
location: Your Location
title: Your Title
mission: Your mission statement
skills:
  Python: 19
  Django: 19
  # etc...
social:
  github-square: username
  linkedin-square: username
```

### Updating Work Experience

Edit `work.yaml`:
```yaml
- company: Company Name
  position: Your Position
  dates: Month Year - Present
  duties:
  - Responsibility or achievement
  - Another item
```

### Modifying Templates

Templates are in `themes/justquick/templates/`. They use Jinja2 syntax.

**Accessing YAML data in templates:**
```jinja2
{{ SITEDATA.info.email }}
{{ SITEDATA.info.skills }}
{% for work in SITEDATA.works %}
  {{ work.company }}
{% endfor %}
```

## Legacy Content Handling

### What is Legacy Content?

The site contains archived documentation for old projects that should NOT be migrated to Markdown/Pelican:

- `django-activity-stream/` - Old project docs (static HTML)
- `google-chartwrapper-apidoc/` - API documentation (static HTML)
- `google-chartwrapper-demos/` - Demo pages (static HTML)
- `jeebusisgod/` - Old project (static HTML)
- `digit/` - Browser game (static assets)
- `gsp.studio/` - Legacy project (static HTML)
- `directories/`, `pdf12step/`, `django-native-tags/` - Archived content

### How Pelican Handles Legacy Content

1. Listed in `STATIC_PATHS` configuration in `pelicanconf.py`
2. Pelican copies these directories verbatim to output without processing
3. URLs remain unchanged (e.g., `/django-activity-stream/index.html` still works)
4. No need to track or maintain - they're frozen snapshots

### Managing Legacy Content

- **To add new legacy directory**: Add to `STATIC_PATHS` in `pelicanconf.py`
- **To remove legacy content**: Remove directory and its entry from `STATIC_PATHS`
- **To update legacy content**: Edit files directly, they'll be copied as-is
- **Never migrate legacy to markdown** - not worth the effort, keep as static files

### Why Keep Legacy Content?

- Historical record of past work
- External links may point to these pages
- Some content may be referenced on the main site
- Low maintenance cost (just static files)

## Local Development

### Setup

```bash
# Install dependencies
uv sync
```

### Development Server

```bash
# Build and serve locally
uv run pelican markdown-content -s pelicanconf.py
uv run pelican --listen

# Visit http://localhost:8000
```

### Auto-Reload on Changes

```bash
# Automatically rebuild when files change
uv run pelican --autoreload --listen
```

### Production Build

```bash
# Build for production with full URLs
uv run pelican markdown-content -s publishconf.py
```

## Deployment

### Automatic Deployment (via GitHub Actions)

The site deploys automatically when you push to the `master` branch:

1. Push changes to GitHub
2. GitHub Actions builds the site using `pelican`
3. Output is deployed to `gh-pages` branch
4. GitHub Pages serves the site

Check the Actions tab on GitHub to see build status.

### Manual Deployment

If needed, you can build and deploy manually:

```bash
# Build the site
uv run pelican markdown-content -s publishconf.py

# The output/ directory contains the built site
# Push this to gh-pages branch or configure GitHub Pages accordingly
```

## Proposed Upgrades

### Phase 1: Basic Migration (CURRENT)
✓ Convert main pages to Markdown
✓ Set up Pelican with custom theme
✓ Implement GitHub Actions deployment
✓ Load YAML data via plugin

### Phase 2: Content Enhancements
- **Blog functionality** for posts about projects/tech
  - Create `markdown-content/blog/` directory
  - Configure Pelican to generate blog index
  - Add RSS/Atom feeds

- **Improved work experience display**
  - Add filtering by year/company
  - Add tags/categories (e.g., Python, DevOps, Django)
  - Create dedicated page per job with details

- **Project showcase section**
  - Replace hardcoded project HTML with markdown files
  - Create reusable project template with GitHub widget integration
  - Auto-fetch GitHub stats via API

### Phase 3: Modern Features
- **Search functionality**
  - Add Lunr.js or similar for client-side search
  - Index blog posts and pages
  - Search box in navigation

- **Dark/light theme toggle**
  - CSS custom properties for theming
  - JavaScript to toggle and persist preference
  - Respect system preference by default

- **Performance optimizations**
  - Minimize/bundle CSS/JS
  - Optimize images (WebP format)
  - Add service worker for offline support

- **Analytics**
  - Privacy-friendly analytics (Plausible or similar)
  - Track popular pages/projects

### Phase 4: Interactive Features
- **Contact form improvements**
  - Replace Formspree with modern alternative
  - Add form validation
  - Success/error messaging

- **Project contributions timeline**
  - Fetch GitHub activity via API
  - Display contribution graph
  - Show recent commits/PRs

- **Skills visualization**
  - Interactive skills chart (D3.js or similar)
  - Filterable by category
  - Show years of experience dynamically

**Implementation Priority:**
1. Complete Phase 1 (basic migration) first
2. Test thoroughly before adding features
3. Implement Phase 2 features one at a time
4. Gather feedback before Phase 3/4
5. Each feature should be in its own branch/PR

## Troubleshooting

### Build Fails

**Check Python version:**
```bash
python --version  # Requires 3.9+
```

**Verify dependencies:**
```bash
uv pip list | grep pelican
uv sync
```

**Check YAML syntax:**
```bash
python -c "import yaml; yaml.safe_load(open('info.yaml'))"
python -c "import yaml; yaml.safe_load(open('work.yaml'))"
```

**Review Pelican error messages:**
```bash
uv run pelican markdown-content -s pelicanconf.py --debug
```

### Missing Legacy Content

- Verify directory exists in root
- Check `STATIC_PATHS` in `pelicanconf.py`
- Ensure `keep_files: true` in `.github/workflows/build.yml`
- Check that the directory is not in `.gitignore`

### YAML Data Not Appearing

- Check plugin is loaded: `PLUGINS = ['yaml_loader']` in `pelicanconf.py`
- Verify YAML syntax (see above)
- Use `{{ SITEDATA.info }}` not `{{ info }}` in templates
- Check that `pelican-plugins/yaml_loader.py` exists

### GitHub Pages Not Updating

- Check GitHub Actions build succeeded (Actions tab)
- Verify GitHub Pages source is set to `gh-pages` branch
- Check for DNS/CNAME issues
- Clear browser cache and do hard refresh
- Check that `.nojekyll` file exists in output

### CSS/JS Not Loading

- Check that `content/` directory exists
- Verify asset paths in templates start with `/content/`
- Ensure `content/` is NOT in `STATIC_PATHS` (it's separate from markdown-content)
- Check browser console for 404 errors

## Tips

- Always test locally before pushing to GitHub
- Keep YAML files well-formatted and validated
- Legacy content should never be modified through Pelican
- Use the development server with `--autoreload` for faster iteration
- Check GitHub Actions logs if deployment fails
- The `output/` directory is gitignored - never commit it

## Resources

- [Pelican Documentation](https://docs.getpelican.com/)
- [Jinja2 Template Documentation](https://jinja.palletsprojects.com/)
- [Markdown Guide](https://www.markdownguide.org/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
