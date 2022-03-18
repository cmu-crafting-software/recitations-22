# Recitation 7: HTML, GitHub Pages, and embedding your data visualization

__Wode "Nimo" Ni__

_22/02/11_

## Github Pages setup

GH Pages is a deployment service that lets you automatically deploy your website.

* Accept the `student-site` assignment: <https://classroom.github.com/a/-PmHW5eA>.
* Go to `student-site-<githubid>` on GitHub and setup GitHub Pages.
  * Settings -> Pages
  * Choose `main` under "Source."
  * Hit "Save."
  * Push an empty commit: `git commit --allow-empty -m "trigger pages"` and `git push`
  * Your page should be up!
  * Reference: <https://docs.github.com/en/pages/quickstart>
* Clone `student-site-<githubid>`

## Quick HTML primer

* HTML (HyperText Markup Language) is the standard markup language for Web pages. It defines the **content** of the webpage.
* Markdown (what you write in `README.md`) actually converts to HTML
* The basic building blocks are similar
  * `<div>`: used as a container for HTML elements - which is then styled with CSS or manipulated with JavaScript
  * Helpful cheatsheet: <https://developer.mozilla.org/en-US/docs/Learn/HTML/Cheatsheet>
* CSS (Cascading Style Sheet): defines the **styling** of HTML components (e.g. color, margin, layout etc.)
  * Selectors: classes, ids, tag types
  * Inline styling
  * The inspecter
* JavaScript: everything else that's fancy, like interactivity and animation.
* More on CSS and JS later! 

## Deploy your visualization

* Export your favorite altair visualization
  * Tutorial: https://altair-viz.github.io/user_guide/saving_charts.html#html-format
  * A vega-lite visualization is actually just a JSON configuration, so either formats will work
  * Write down something that describes your visualization and include that in your webpage

