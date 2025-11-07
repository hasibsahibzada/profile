# Hasibullah Sahibzada - Professional Portfolio

A modern, responsive portfolio website built with Jekyll and Markdown. Features a dark theme, portfolio showcase, professional experiences, and a blog section.

## Features

- 🎨 **Dark Theme** - Modern dark theme with gradient accents
- 📱 **Responsive Design** - Fully responsive across all devices
- 🚀 **Portfolio Section** - Showcase your projects using Markdown files
- 💼 **Experiences Section** - Display your professional journey
- 📝 **Blog/Posts Section** - Share your thoughts and insights
- ⚡ **Simple Content Management** - Easy to update with Markdown files
- 🔄 **Auto Deployment** - Automatic deployment to GitHub Pages

## Tech Stack

- **Jekyll** - Static site generator
- **Markdown** - Simple content authoring
- **CSS** - Custom dark theme styling
- **GitHub Pages** - Free hosting

## Getting Started

### Prerequisites

- Ruby 3.1 or higher
- Bundler gem

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/profile.git
cd profile
```

2. Install dependencies:
```bash
bundle install
```

3. Start the Jekyll server:
```bash
bundle exec jekyll serve
```

4. Open your browser and navigate to `http://localhost:4000/profile/`

## Content Management

### Update Your Profile

Edit `_config.yml` to update:
- Personal information (name, title, bio, photo)
- Social media links
- Site settings

### Add Portfolio Items

Create new Markdown files in `_portfolio/` directory:

```markdown
---
title: Project Name
excerpt: Short description
image: /assets/images/portfolio-1.jpg
technologies:
  - Angular
  - TypeScript
project_url: https://example.com
github_url: https://github.com/example
featured: true
---

Full project description here.
```

### Add Experiences

Create new Markdown files in `_experiences/` directory:

```markdown
---
company: Company Name
position: Job Title
location: Location
start_date: 2020-01-01
current: true
technologies:
  - Angular
  - TypeScript
logo: /assets/images/company-1.jpg
---

## Responsibilities

- Responsibility 1
- Responsibility 2
```

### Add Blog Posts

Create new Markdown files in `_posts/` directory with format: `YYYY-MM-DD-post-title.md`:

```markdown
---
title: Post Title
excerpt: Short excerpt
date: 2024-01-15
author: Hasibullah Sahibzada
tags:
  - Angular
  - TypeScript
image: /assets/images/post-1.jpg
featured: true
---

Your post content here in Markdown format.
```

## Adding Images

Place your images in the `assets/images/` directory:
- `profile-photo.jpg` - Your profile photo
- `portfolio-*.jpg` - Portfolio project images
- `post-*.jpg` - Blog post images
- `company-*.jpg` - Company logos

## Customization

### Theme Colors

Edit `assets/css/main.css` to customize colors:
- `--bg-primary` - Primary background color
- `--bg-secondary` - Secondary background color
- `--accent-primary` - Primary accent color
- `--accent-secondary` - Secondary accent color

## GitHub Pages Deployment

The site automatically deploys to GitHub Pages when you push to the `main` branch.

### Setup Instructions

1. Go to your repository settings on GitHub
2. Navigate to **Pages** under **Settings**
3. Under **Source**, select **GitHub Actions**
4. The workflow will automatically deploy when you push to `main`

## Project Structure

```
.
├── _config.yml              # Site configuration
├── _layouts/                # Page layouts
│   ├── default.html
│   └── post.html
├── _includes/               # Reusable components
│   ├── header.html
│   └── footer.html
├── _portfolio/              # Portfolio items (Markdown)
├── _experiences/            # Experiences (Markdown)
├── _posts/                  # Blog posts (Markdown)
├── assets/
│   ├── css/                 # Stylesheets
│   └── images/              # Images
├── index.html               # Home page
├── portfolio.html           # Portfolio page
├── experiences.html         # Experiences page
└── posts.html               # Posts listing page
```

## License

This project is open source and available under the MIT License.

## Contact

- **Name**: Hasibullah Sahibzada
- **LinkedIn**: [LinkedIn Profile](https://www.linkedin.com/in/hasibullah-sahibzada-1a85a242/)
- **Xing**: [Xing Profile](https://www.xing.com/profile/Hasibullah_Sahibzada/web_profiles)
