******************************
基本的な使い方
******************************

インポート
==========

はじめに，NIMS-OSをインポートします．

.. code-block:: python

    import nimsos


各種パラメータを定義
==========================

* ``ObjectivesNum``: 目的関数の個数を指定します．
* ``ProposalsNum``: 一度のサイクルで人工知能が提案する実験条件数を指定します．これはロボット実験における並列実験数に対応します．
* ``CyclesNum``: サイクル数を指定します．

例えば，目的関数の個数が２つであり，並列実験数を２とする場合，
３回サイクルを回し最適化を実施する場合は，
以下のように設定する．

.. code-block:: python

    ObjectivesNum = 2
    ProposalsNum = 2
    CyclesNum = 3


実験条件ファイルを指定
======================================================

``candidates_file`` に実験条件をリスト化したファイルを指定します．

実験条件ファイルは，以下のようにあらかじめ用意します．
:math:`d` 次元のdescriptorがあり，:math:`l` 個の目的関数を考える場合を例としています．
初めの:math:`d` 列にdescriptorの候補を全て入力します．
これが材料の探索空間となり，この部分には空欄が無いようにします．
続く:math:`l` 列は，目的関数の値を入力します．
初期段階で実験データが全くない場合，目的関数の部分は空欄となります．


+----------------+-------+----------------------+-------------+------+---------------------+
| descriptor 1   | ...   | descriptor :math:`d` | objective 1 | ...  | objective :math:`l` |
+================+=======+======================+=============+======+=====================+
| 1              | ...   | 0                    |             |      |                     |
+----------------+-------+----------------------+-------------+------+---------------------+
| 1              | ...   | 0.5                  |             |      |                     |
+----------------+-------+----------------------+-------------+------+---------------------+
| 1              | ...   | 1                    |             |      |                     |
+----------------+-------+----------------------+-------------+------+---------------------+
| 0.5            | ...   | 0                    |             |      |                     |
+----------------+-------+----------------------+-------------+------+---------------------+
| 0.5            | ...   | 0.5                  |             |      |                     |
+----------------+-------+----------------------+-------------+------+---------------------+
| 0.5            | ...   | 1                    |             |      |                     |
+----------------+-------+----------------------+-------------+------+---------------------+
| 0              | ...   | 0                    |             |      |                     |
+----------------+-------+----------------------+-------------+------+---------------------+
| 0              | ...   | 0.5                  |             |      |                     |
+----------------+-------+----------------------+-------------+------+---------------------+
| 0              | ...   | 1                    |             |      |                     |
+----------------+-------+----------------------+-------------+------+---------------------+



例えば，実験条件ファイルの名前をcandidates.csvとし，
メインスクリプトと同じフォルダに格納する場合は，以下のように設定します．

.. code-block:: python

    candidates_file = "./candidates.csv"


もし，実験データがいくつか得られている場合は，以下のように :math:`l` 個の全ての目的関数を入力します．

+----------------+-------+----------------------+-------------+------+---------------------+
| descriptor 1   | ...   | descriptor :math:`d` | objective 1 | ...  | objective :math:`l` |
+================+=======+======================+=============+======+=====================+
| 1              | ...   | 0                    |             |      |                     |
+----------------+-------+----------------------+-------------+------+---------------------+
| 1              | ...   | 0.5                  | 12          | ...  | 20                  |
+----------------+-------+----------------------+-------------+------+---------------------+
| 1              | ...   | 1                    |             |      |                     |
+----------------+-------+----------------------+-------------+------+---------------------+
| 0.5            | ...   | 0                    |             |      |                     |
+----------------+-------+----------------------+-------------+------+---------------------+
| 0.5            | ...   | 0.5                  |             |      |                     |
+----------------+-------+----------------------+-------------+------+---------------------+
| 0.5            | ...   | 1                    | 5           | ...  | 8                   |
+----------------+-------+----------------------+-------------+------+---------------------+
| 0              | ...   | 0                    |             |      |                     |
+----------------+-------+----------------------+-------------+------+---------------------+
| 0              | ...   | 0.5                  |             |      |                     |
+----------------+-------+----------------------+-------------+------+---------------------+
| 0              | ...   | 1                    | 23          | ...  | 2                   |
+----------------+-------+----------------------+-------------+------+---------------------+


人工知能による提案ファイルを指定
======================================================

``proposals_file``  に人工知能が提案する条件を記載するファイルを指定します．
このファイルは，NIMS-OSにより作成されるため，ファイルをあらかじめ作成する必要はなく，
名前を指定するだけになります．

例えば，メインスクリプトと同じフォルダにproposals.csvという名前で格納する場合は，以下のように設定します．

.. code-block:: python

    proposals_file = "./proposals.csv"



ロボット実験用データの保管場所を指定
======================================================

* ``input_folder``: ロボット実験における入力ファイルを格納するフォルダを指定します．
* ``output_folder``: ロボット実験からの出力ファイルを格納するフォルダを指定します．

例えば，入力用のフォルダを./EXPInputとし，出力用のフォルダを./EXPOutputとする場合，
以下のように指定します．

.. code-block:: python

    input_folder = "./EXPInput"
    output_folder = "./EXPOutput"



人工知能の実行
======================================================

``nimsos.selection`` を利用し，人工知能による実験条件の提案を計算します．

引数
^^^^^^^^

* ``method``: 人工知能の手法を指定します．"PHYSBO": PHYSBOによるベイズ最適化，"BLOX": BLOXによる無目的探索，"PDC": PDCによる相図作成， "RE": ランダム探索が指定できます．
* ``input_file``: 実験条件ファイル"candidates_file"を指定します．
* ``output_file``: 人工知能からの提案ファイル"proposals_file"を指定します．
* ``num_objectives``: 目的関数の個数"ObjectivesNum"を指定します．もちろん，直接，値を指定することもできます．
* ``num_proposals``: 一度のサイクルで人工知能が提案する条件数"ProposalsNum"を指定します．もちろん，直接，値を指定することもできます．

例えば，ベイズ最適化による提案を計算する場合は以下のように指定します．

.. code-block:: python

    nimsos.selection(method = "PHYSBO", 
                     input_file = candidates_file, 
                     output_file = proposals_file,
                     num_objectives = ObjectivesNum, 
                     num_proposals = ProposalsNum)




ロボット実験用インプットファイルの作成およびロボット実験の実行
====================================================================

``nimsos.preparation_input`` を利用し，ロボット実験用インプットファイルを作成し，ロボット実験を実行します．

この部分は， **扱うロボットに依存して書き換える必要** があります．

引数
^^^^^^^^

* ``machine``: 使用するロボットを指定します．"STAN": 標準形式のモジュール，"NAREE": NIMS電気化学自動実験ロボット用のモジュールが指定できます．
* ``input_file``: 人工知能からの提案ファイル"proposals_file"を指定します．
* ``input_folder``: ロボット実験における入力ファイルを格納するフォルダ"input_folder"を指定します．

例えば，標準形式のモジュールを使用する場合は以下のように指定します．

.. code-block:: python

    nimsos.preparation_input(machine = "STAN", 
                             input_file = proposals_file, 
                             input_folder = input_folder)


ロボット実験結果の解析と実験条件ファイルの更新
====================================================================

``nimsos.analysis_output`` を利用し，ロボット実験の結果を解析し，実験条件ファイルを更新します．

この部分は， **扱うロボットに依存して書き換える必要** があります．

引数
^^^^^^^^

* ``machine``: 使用するロボットを指定します．（"STAN": 標準形式のモジュール，"NAREE": NIMS電気化学自動実験ロボット用のモジュール）
* ``input_file``: 人工知能からの提案ファイル"proposals_file"を指定します．
* ``output_file``: 実験条件ファイル"candidates_file"を指定します．
* ``num_objectives``: 目的関数の個数"ObjectivesNum"を指定します．もちろん，直接，値を指定することもできます．
* ``output_folder``: ロボット実験からの出力ファイルを格納するフォルダ"output_folder"を指定します．
* ``objectives_info``: "NAREE"を指定した場合に，実験結果のうちどの特性を目的関数として利用するかを指定します．辞書形式で指定する必要があります．


例えば，標準形式のモジュールを使用する場合は以下のように指定します．

.. code-block:: python

    nimsos.analysis_output(machine = "STAN", 
                           input_file = proposals_file, 
                           output_file = candidates_file,
                           num_objectives = ObjectivesNum, 
                           output_folder = output_folder)



結果履歴の格納・更新
======================================================

``nimsos.history`` を利用することで，最適化結果の履歴を保存できます．

引数
^^^^^^^^

* ``input_file``: 実験条件ファイル"candidates_file"を指定します．
* ``num_objectives``: 目的関数の個数"ObjectivesNum"を指定します．もちろん，直接，値を指定することもできます．
* ``itt``: 現在のサイクル数を入力します．指定しない場合，新しく履歴を保存するリストが作成されます．
* ``history_file``: すでに ``history_file`` を作成済みな場合，ここで指定することで，ファイルが更新されます．指定しない場合，新しく履歴を保存するリストが作成されます．

具体的には，初めて最適化結果を格納する場合以下のように実行します．

.. code-block:: python

    res_history = nimsos.history(input_file = candidates_file, 
                                 num_objectives = ObjectivesNum)


``res_history`` を更新する場合，

Kサイクル目に ``res_history`` を更新する場合，
以下のように実行します．

.. code-block:: python

    res_history = nimsos.history(input_file = candidates_file, 
                                 num_objectives = ObjectivesNum, 
                                 itt = K, 
                                 history_file = res_history)




結果の可視化
======================================================

``nimsos.visualization`` を利用することで，結果を可視化することができます．
メインスクリプトと同じフォルダに ``fig`` という名前のフォルダを作成してください．
その中に図が出力されることになります．


履歴の可視化
^^^^^^^^^^^^^^^^^


``nimsos.visualization.plot_history`` を利用することで，履歴を可視化することができます．

* ``nimsos.visualization.plot_history.cycle``: 全データのサイクル依存性をプロットすることができます．

* ``nimsos.visualization.plot_history.best``: 各サイクルにおける最大値をプロットすることができます．

引数
------------

* ``input_file``: 履歴を格納したファイル"res_history"を指定します．
* ``num_cycles``: サイクル数"CyclesNum"を指定します．


具体的には，以下のように実行します．


.. code-block:: python

    nimsos.visualization.plot_history.cycle(input_file = res_history, 
                                            num_cycles = CyclesNum)

    nimsos.visualization.plot_history.best(input_file = res_history, 
                                           num_cycles = CyclesNum)




目的関数の分布の可視化
^^^^^^^^^^^^^^^^^^^^^^^^^^^


``nimsos.visualization.plot_distribution.plot`` を利用することで，目的関数値の分布を可視化することができます．
目的関数が１次元の場合は，ヒストグラムとして，２次元，３次元の場合はscatter plotとして出力されます．
４次元以上は指定しても図は出力されません．


引数
------------

* ``input_file``: 実験条件ファイル"candidates_file"を指定します．
* ``num_objectives``: 目的関数の個数"ObjectivesNum"を指定します．


具体的には，以下のように実行します．


.. code-block:: python

    nimsos.visualization.plot_distribution.plot(input_file = candidates_file, 
                                                num_objectives = ObjectivesNum)




相図の可視化
^^^^^^^^^^^^^^^^^^^^^^^^^^^


``nimsos.visualization.plot_phase_diagram.plot`` を利用することで，予測相図を出力することができます．
人工知能の方法としてPDCを利用する場合に利用できます．
descriptorの次元が１次元の場合，４次元以上の場合は出力されません．


引数
------------

* ``input_file``: 実験条件ファイル"candidates_file"を指定します．


具体的には，以下のように実行します．


.. code-block:: python

    nimsos.visualization.plot_phase_diagram.plot(input_file = candidates_file)





自作モジュールを利用する場合
====================================================================


``ai_tool_original.py`` の作成
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

自作のAIを利用する場合， ``ai_tool_original.py`` を作成しメインスクリプトと同じフォルダに格納してください．
最も基本的な ``ai_tool_re.py`` を適切に書き換えて作成してください．
クラス名は以下のように ``ORIGINAL`` とすることで，GUI版でも使用することができます．

.. code-block:: python

    class ORIGINAL():



以下のように実行します．

.. code-block:: python

     import ai_tool_original
     ai_tool_original.ORIGINAL(input_file = candidates_file,
                               output_file = proposals_file,
                               num_objectives = ObjectivesNum,
                               num_proposals = ProposalsNum).select()



``preparation_input_original.py`` の作成
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

自作のロボット実験装置を利用する場合， ``preparation_input_original.py`` を作成しメインスクリプトと同じフォルダに格納してください．
最も基本的な ``preparation_input_standard.py`` を適切に書き換えて作成してください．
クラス名は以下のように ``ORIGINAL`` とすることで，GUI版でも使用することができます．

.. code-block:: python

    class ORIGINAL():



以下のように実行します．

.. code-block:: python

    import preparation_input_original
    preparation_input_original.ORIGINAL(input_file = proposals_file,
                                        input_folder = input_folder).perform()


``analysis_output_original.py`` の作成
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

自作のロボット実験装置を利用する場合， ``analysis_output_original.py`` を作成しメインスクリプトと同じフォルダに格納してください．
最も基本的な ``analysis_output_standard.py`` を適切に書き換えて作成してください．
クラス名は以下のように ``ORIGINAL`` とすることで，GUI版でも使用することができます．

.. code-block:: python

    class ORIGINAL():



以下のように実行します．

.. code-block:: python

    import analysis_output_original
    analysis_output_original.ORIGINAL(input_file = proposals_file,
                                      output_file = candidates_file,
                                      num_objectives = ObjectivesNum,
                                      output_folder = output_folder).perform()

