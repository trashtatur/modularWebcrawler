function stopCrawlers() {
            $.ajax({
            url: '/stopCrawler',
            data:  "",
            type: 'POST',
            success: function(response) {
                console.log(response);
                console.log("SUCCESS")
            },
            error: function(error) {
                console.log(error);
                console.log("FAILURE")
            }
        });
}