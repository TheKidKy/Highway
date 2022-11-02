// function addPostComment(postId) {
//     let comment = $('#commentText').val();
//
//     $.get('/blog/add-post-comment', {
//         post_comment: comment,
//         post_id: postId
//     }).then(res => {
//         $('.comments').html(res);
//         $('#commentText').val('');
//         location.reload();
//     });
// }