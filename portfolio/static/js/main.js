let totalSection;
let allSection;

document.addEventListener("DOMContentLoaded", function() {
      // Check if Typed is available before using it
      if (typeof Typed !== 'undefined') {
          var typed = new Typed('.typing', {
                strings: [
                    'Inspiration',
                    'Innovation',
                    'Impact',
                    'Créativité',
                    'Qualité',
                    'Rapidité',
                    'Discretion'
                ],
                typeSpeed: 100,
                backSpeed: 60,
                loop: true
            });
      }
        
        

    const nav = document.querySelector(".nav");
    
    if (nav) {
        const navList = nav.querySelectorAll('li'); // Use querySelectorAll for multiple elements
        const totalNavList = navList.length;
        allSection = document.querySelectorAll(".section");
        totalSection = allSection.length;
        
        for (let i = 0; i < totalNavList; i++) {

            const a = navList[i].querySelector('a');
            if (a) { // Check if anchor element exists
                a.addEventListener("click", function() {
                    for (let j = 0; j < totalNavList; j++) {
                        if (allSection[j]) { // Check if section exists
                            allSection[j].classList.remove("back-section");
                        }
                    }

                    for (let j = 0; j < totalNavList; j++) {
                        const navAnchor = navList[j].querySelector('a');
                        if (navAnchor && navAnchor.classList.contains("active")) {
                            if (allSection[j]) { // Check if section exists
                                allSection[j].classList.add("back-section");
                            }
                        }
                        if (navAnchor) { // Check if anchor exists
                            navAnchor.classList.remove("active");
                        }
                    }
                    this.classList.add("active");
                    showSection(this);
                });
            }
        }
        
        function showSection(element) {
            if (!element) return; // Check if element exists
            
            for (let i = 0; i < totalSection; i++) {
                if (allSection[i]) { // Check if section exists
                    allSection[i].classList.remove("active");
                }
            }
            
            const href = element.getAttribute("href");
            if (href) { // Check if href exists
                console.log(href);
                const target = href.split("#")[1];
                if (target) { // Check if target exists
                    const targetElement = document.querySelector("#" + target);
                    if (targetElement) { // Check if target element exists
                        targetElement.classList.add("active");
                    }
                }
            }
            
            if(window.innerWidth < 1200) {
                asideSectionTogglerBtn();
            }
        }
    } else {
        console.error("Navigation element not found.");
    }

    const navTogglerBtn = document.querySelector(".nav-toggler");
    const aside = document.querySelector(".aside");

    if (navTogglerBtn && aside) { // Check if elements exist
        navTogglerBtn.addEventListener("click", () => {
            asideSectionTogglerBtn();
        });
    }

    function asideSectionTogglerBtn() {
        if (aside && navTogglerBtn) { // Check if elements exist
            aside.classList.toggle("open");
            navTogglerBtn.classList.toggle("open");
            for (let i = 0; i < totalSection; i++) {
                if (allSection[i]) { // Check if section exists
                    allSection[i].classList.toggle("open");
                }
            }
        }
    }

    const filterButtons = document.querySelectorAll('.portfolio-filter button');
    const portfolioItems = document.querySelectorAll('.portfolio-item');

    if (filterButtons.length > 0 && portfolioItems.length > 0) { // Check if elements exist
        filterButtons.forEach(button => {
            if (button) { // Check if button exists
                button.addEventListener('click', function() {
                    // Remove active class from all buttons
                    filterButtons.forEach(btn => {
                        if (btn) { // Check if button exists
                            btn.classList.remove('active');
                        }
                    });

                    // Add active class to the clicked button
                    this.classList.add('active');

                    const filterValue = this.getAttribute('data-filter');

                    // Filter portfolio items
                    portfolioItems.forEach(item => {
                        if (item) { // Check if item exists
                            const category = item.getAttribute('data-category');
                            
                            if (filterValue === 'all' || category === filterValue) {
                                item.style.display = 'block';
                            } else {
                                item.style.display = 'none';
                            }
                        }
                    });
                });
            }
        });
    }
});
