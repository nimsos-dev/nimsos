******************************
インストール
******************************

インストール
==================

必要パッケージ
-----------------

* Python >= 3.6
* Cython
* matplotlib
* numpy
* physbo
* scikit-learn
* scipy



.. _install_jp:

インストール手順
------------------

* ``PyPI`` からのインストール（依存パッケージも同時にインストールされます．）

.. code-block:: python

    pip3 install nimsos



* ``--user`` オプションを追加するとユーザのホームディレクトリ以下にインストールされます．

.. code-block:: python

    pip3 install --user nimsos



Windows PCの場合
------------------

* Visual Studioのインストール

Windows PCでは上記pipでインストールできない場合があります．
これは，PHYSBOがCythonを利用しているため，C++コンパイラが必要なためです．
MicrosoftのサイトよりVisual Studioをインストールすることで，pipでインストール可能となります．

https://visualstudio.microsoft.com/ja/



アンインストール
=====================


* 以下のコマンドを実行します。

.. code-block:: python

   pip uninstall nimsos

