function changeToText(imgUrl) {
    const link = document.createElement('a');
    link.href = imgUrl;
    link.download = imgUrl.substring(imgUrl.lastIndexOf('/') + 1);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}