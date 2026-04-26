document.addEventListener('DOMContentLoaded', function() {
  // TOC collapsible functionality
  function makeTOCCollapsible() {
    const tocContent = document.querySelector('.toc-content');
    if (!tocContent) return;

    // Find all ul elements that are direct children of the nav
    const nav = tocContent.querySelector('#TableOfContents');
    if (!nav) return;

    const topLevelUls = Array.from(nav.children).filter(child => child.tagName === 'UL');

    topLevelUls.forEach(function(ul, index) {
      // Skip the first ul (usually just contains the first item)
      if (index === 0) return;

      // Find the previous element (should be another ul or text)
      const prevUl = topLevelUls[index - 1];
      if (!prevUl) return;

      // Get the last li from the previous ul
      const lastLi = prevUl.querySelector('li:last-child');
      if (!lastLi) return;

      // Create a toggle element from the last li's content
      const toggle = document.createElement('div');
      toggle.className = 'toc-toggle';
      toggle.innerHTML = lastLi.innerHTML;
      toggle.setAttribute('data-target', 'toc-submenu-' + index);

      // Replace the last li with the toggle
      lastLi.parentNode.replaceChild(toggle, lastLi);

      // Add classes to the ul
      ul.className = 'toc-submenu';
      ul.id = 'toc-submenu-' + index;

      // Add click handler
      toggle.addEventListener('click', function() {
        this.classList.toggle('expanded');
        ul.classList.toggle('expanded');
      });
    });
  }

  // Auto-expand TOC sections based on current scroll position
  function updateTOC() {
    const headings = document.querySelectorAll('h1, h2, h3, h4, h5, h6');
    const tocLinks = document.querySelectorAll('.toc a');

    let currentHeading = null;
    const scrollPosition = window.scrollY + 100;

    // Find the current heading
    for (let i = headings.length - 1; i >= 0; i--) {
      const heading = headings[i];
      if (heading.offsetTop <= scrollPosition) {
        currentHeading = heading;
        break;
      }
    }

    // Update active link
    tocLinks.forEach(link => {
      link.classList.remove('active');
      if (currentHeading && link.getAttribute('href') === '#' + currentHeading.id) {
        link.classList.add('active');
      }
    });
  }

  // Initialize TOC
  makeTOCCollapsible();

  // Throttle scroll events
  let scrollTimer;
  window.addEventListener('scroll', function() {
    clearTimeout(scrollTimer);
    scrollTimer = setTimeout(updateTOC, 50);
  });

  // Initial update
  updateTOC();
});