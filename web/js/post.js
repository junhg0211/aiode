const postsNav = document.getElementsByClassName("posts-nav")[0];

(function () {
    if (typeof NOW_PAGE !== "undefined") {
        if (postsNav !== undefined) {
            let previousButton = postsNav.children[0].children[0];
            if (parseInt(previousButton.innerText) < 1) {
                previousButton.disabled = true;
            }

            if (ARTICLE_PER_PAGE * NOW_PAGE >= ARTICLE_COUNT) {
                let nextButton = postsNav.children[2].children[0];
                nextButton.disabled = true;
            }
        }
    }
})();