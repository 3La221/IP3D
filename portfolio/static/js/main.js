let totalSection;
let allSection;

document.addEventListener("DOMContentLoaded", function() {
      var typed = new Typed('.typing', {
            strings: [
                'Inspiration',
                'Innovation',
                'Impact',
                'Créativité',
                'Succès',
                'Excellence'
            ],
            typeSpeed: 100,
            backSpeed: 60,
            loop: true
        });
        
        

    const nav = document.querySelector(".nav");
    
    if (nav) {
        const navList = nav.querySelectorAll('li'); // Use querySelectorAll for multiple elements
        const totalNavList = navList.length;
        allSection = document.querySelectorAll(".section");
        totalSection = allSection.length;
        
        for (let i = 0; i < totalNavList; i++) {

            const a = navList[i].querySelector('a');
            a.addEventListener("click", function() {
                for (let j = 0; j < totalNavList; j++) {
                    allSection[j].classList.remove("back-section");
                }

                for (let j = 0; j < totalNavList; j++) {
                    if (navList[j].querySelector('a').classList.contains("active")) {
                        allSection[j].classList.add("back-section");
                    }
                    navList[j].querySelector('a').classList.remove("active"); 
                }
                this.classList.add("active");
                showSection(this);
            });
        }
        
        function showSection(element) {
            for (let i = 0; i < totalSection; i++) {
                allSection[i].classList.remove("active");
            }
            console.log(element.getAttribute("href"));
            const target = element.getAttribute("href").split("#")[1];
            document.querySelector("#" + target).classList.add("active");
            if(window.innerWidth < 1200) {
                asideSectionTogglerBtn();
            }
        }
    } else {
        console.error("Navigation element not found.");
    }

    const navTogglerBtn = document.querySelector(".nav-toggler");
    const aside = document.querySelector(".aside");

    navTogglerBtn.addEventListener("click", () => {
        asideSectionTogglerBtn();
    });

    function asideSectionTogglerBtn() {
        aside.classList.toggle("open");
        navTogglerBtn.classList.toggle("open");
        for (let i = 0; i < totalSection; i++) {
            allSection[i].classList.toggle("open");
        }
    }

    const filterButtons = document.querySelectorAll('.portfolio-filter button');
    const portfolioItems = document.querySelectorAll('.portfolio-item');

    filterButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Remove active class from all buttons
            filterButtons.forEach(btn => btn.classList.remove('active'));

            // Add active class to the clicked button
            this.classList.add('active');

            const filterValue = this.getAttribute('data-filter');

            // Filter portfolio items
            portfolioItems.forEach(item => {
                const category = item.getAttribute('data-category');

                if (filterValue === 'all' || category === filterValue) {
                    item.style.display = 'block';
                } else {
                    item.style.display = 'none';
                }
            });
        });
    });
});
