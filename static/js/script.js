/* 
 * [The modals.js javascript file consists of all event
 * listeners and functions used for the showing
 * and hiding of  confirmation modals]
 */


/*
 * [This function is used to confirm post deletion]
 */
document.getElementById("post-delete-id").addEventListener('click',
    function deletePost() {
        if (window.confirm("Do you really want to delete this post from your profile?")) {
            window.location.href = "/";
        }
    });