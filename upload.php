<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<script type="text/python" src="pyton/mosaic_detect.py"></script>

<title>sample</title>
</head>
<body>
  <!-- 保存処理 -->
<p><?php
if (is_uploaded_file($_FILES["upfile"]["tmp_name"])) {
  if (move_uploaded_file($_FILES["upfile"]["tmp_name"], "files/" . "data.jpeg")) {
  // if (move_uploaded_file($_FILES["upfile"]["tmp_name"], "files/" . $_FILES["upfile"]["name"])) {
    // chmod("files/" . $_FILES["upfile"]["name"], 0644);
    chmod("files/" . "data.png", 0644);
    echo $_FILES["upfile"]["name"] . "をアップロードしました。";
  } else {
    echo "ファイルをアップロードできません。";
  }
} else {
  echo "ファイルが選択されていません。";
}
?>
</p>
<!-- 表示処理 -->
<p>アップロードされたファイルはこちら</p>
<p><img src="./files/data.png"/></p>


<button id="execute">計算だ!</button>

<a href="index.php">トップへ</a>
</body>
</html>
