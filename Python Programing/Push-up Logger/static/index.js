<style>
    document.addEventListener('DOMContentLoaded', function() {
    const imageLinks = document.querySelectorAll('.image-link');

    imageLinks.forEach(link => {
        const hoverImage = link.querySelector('.hover-image');

        link.addEventListener('mouseenter', function() {
            hoverImage.src = "{{ url_for('static', filename='sololearn.png') }}";
        });

        link.addEventListener('mouseleave', function() {
            hoverImage.src = "{{ url_for('static', filename='image1.jpg') }}";
        });
    });
});
</style>