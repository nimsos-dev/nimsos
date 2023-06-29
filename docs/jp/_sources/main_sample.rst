******************************
メインスクリプト例
******************************


ベイズ最適化の場合
====================

.. code-block:: python

    import nimsos

    #目的関数の数を指定します．
    ObjectivesNum = 2

    #一度のサイクルで人工知能が提案する条件数を指定します．
    ProposalsNum = 2

    #サイクル数を指定します．
    CyclesNum = 3


    #実験条件をリスト化したファイルを指定
    candidates_file = "./candidates.csv"

    #人工知能が提案する条件を記載するファイルを指定
    proposals_file = "./proposals.csv"


    #ロボット実験における入力ファイルを格納するフォルダを指定
    input_folder = "./EXPInput"

    #ロボット実験からの出力ファイルを格納するフォルダを指定
    output_folder = "./EXPOutput"


    #履歴を格納するリストを作成
    res_history = nimsos.history(input_file = candidates_file, 
                                 num_objectives = ObjectivesNum)

    for K in range(CyclesNum):

        print("Start cycle", K+1)

        #最初のサイクルは実験データがないため，ランダム探索を実施
        #初めから実験データがいくつかある場合は，最初からPHYSBOを実行可能であり，分岐の必要は無し
        if K==0:
            method = "RE"
        else:
            method = "PHYSBO"

        #人工知能の実行            
        nimsos.selection(method = method, 
                         input_file = candidates_file, 
                         output_file = proposals_file,
                         num_objectives = ObjectivesNum, 
                         num_proposals = ProposalsNum)


        #ロボット実験用インプットファイルの作成およびロボット実験の実行
        nimsos.preparation_input(machine = "STAN", 
                                 input_file = proposals_file, 
                                 input_folder = input_folder)

        #ロボット実験結果の解析と実験条件ファイルの更新
        nimsos.analysis_output(machine = "STAN", 
                               input_file = proposals_file, 
                               output_file = candidates_file,
                               num_objectives = ObjectivesNum, 
                               output_folder = output_folder)

        #履歴を格納するリストを更新
        res_history = nimsos.history(input_file = candidates_file, 
                                     num_objectives = ObjectivesNum, 
                                     itt = K, 
                                     history_file = res_history)

        #各サイクルの目的関数のデータ分布を出力
        nimsos.visualization.plot_distribution.plot(input_file = candidates_file, 
                                                    num_objectives = ObjectivesNum)


    #目的関数のサイクル依存性をプロット
    nimsos.visualization.plot_history.cycle(input_file = res_history, 
                                            num_cycles = CyclesNum)

    #目的関数の最大値のサイクル依存性をプロット
    nimsos.visualization.plot_history.best(input_file = res_history, 
                                           num_cycles = CyclesNum)





無目的探索の場合
====================

.. code-block:: python

    import nimsos

    #目的関数の数を指定します．
    ObjectivesNum = 2

    #一度のサイクルで人工知能が提案する条件数を指定します．
    ProposalsNum = 2

    #サイクル数を指定します．
    CyclesNum = 3


    #実験条件をリスト化したファイルを指定
    candidates_file = "./candidates.csv"

    #人工知能が提案する条件を記載するファイルを指定
    proposals_file = "./proposals.csv"


    #ロボット実験における入力ファイルを格納するフォルダを指定
    input_folder = "./EXPInput"

    #ロボット実験からの出力ファイルを格納するフォルダを指定
    output_folder = "./EXPOutput"


    #履歴を格納するリストを作成
    res_history = nimsos.history(input_file = candidates_file, 
                                 num_objectives = ObjectivesNum)

    for K in range(CyclesNum):

        print("Start cycle", K+1)

        #最初のサイクルは実験データがないため，ランダム探索を実施
        #初めから実験データがいくつかある場合は，最初からBLOXを実行可能であり，分岐の必要は無し
        if K==0:
            method = "RE"
        else:
            method = "BLOX"

        #人工知能の実行
        nimsos.selection(method = method, 
                         input_file = candidates_file, 
                         output_file = proposals_file,
                         num_objectives = ObjectivesNum, 
                         num_proposals = ProposalsNum)

        #ロボット実験用インプットファイルの作成およびロボット実験の実行
        nimsos.preparation_input(machine = "STAN", 
                                 input_file = proposals_file, 
                                 input_folder = input_folder)

        #ロボット実験結果の解析と実験条件ファイルの更新
        nimsos.analysis_output(machine = "STAN", 
                               input_file = proposals_file, 
                               output_file = candidates_file,
                               num_objectives = ObjectivesNum, 
                               output_folder = output_folder)

        #履歴を格納するリストを更新
        res_history = nimsos.history(input_file = candidates_file, 
                                     num_objectives = ObjectivesNum, 
                                     itt = K, 
                                     history_file = res_history)

        #各サイクルの目的関数のデータ分布を出力
        nimsos.visualization.plot_distribution.plot(input_file = candidates_file, 
                                                    num_objectives = ObjectivesNum)


    #目的関数のサイクル依存性をプロット
    nimsos.visualization.plot_history.cycle(input_file = res_history, 
                                            num_cycles = CyclesNum)

    #目的関数の最大値のサイクル依存性をプロット
    nimsos.visualization.plot_history.best(input_file = res_history, 
                                           num_cycles = CyclesNum)




相図作成の場合
====================

.. code-block:: python

    import nimsos

    #目的関数の数を指定します．
    ObjectivesNum = 2

    #一度のサイクルで人工知能が提案する条件数を指定します．
    ProposalsNum = 2

    #サイクル数を指定します．
    CyclesNum = 3


    #実験条件をリスト化したファイルを指定
    candidates_file = "./candidates.csv"

    #人工知能が提案する条件を記載するファイルを指定
    proposals_file = "./proposals.csv"


    #ロボット実験における入力ファイルを格納するフォルダを指定
    input_folder = "./EXPInput"

    #ロボット実験からの出力ファイルを格納するフォルダを指定
    output_folder = "./EXPOutput"


    #履歴を格納するリストを作成
    res_history = nimsos.history(input_file = candidates_file, 
                                 num_objectives = ObjectivesNum)

    for K in range(CyclesNum):

        print("Start cycle", K+1)

        #最初のサイクルは実験データがないため，ランダム探索を実施
        #初めから実験データがいくつかある場合は，最初からPDCを実行可能であり，分岐の必要は無し
        if K==0:
            method = "RE"
        else:
            method = "PDC"

        #人工知能の実行
        nimsos.selection(method = method, 
                         input_file = candidates_file, 
                         output_file = proposals_file,
                         num_objectives = ObjectivesNum, 
                         num_proposals = ProposalsNum)

        #ロボット実験用インプットファイルの作成およびロボット実験の実行
        nimsos.preparation_input(machine = "STAN", 
                                 input_file = proposals_file, 
                                 input_folder = input_folder)

        #ロボット実験結果の解析と実験条件ファイルの更新
        nimsos.analysis_output(machine = "STAN", 
                               input_file = proposals_file, 
                               output_file = candidates_file,
                               num_objectives = ObjectivesNum, 
                               output_folder = output_folder)

        #履歴を格納するリストを更新
        res_history = nimsos.history(input_file = candidates_file, 
                                     num_objectives = ObjectivesNum, 
                                     itt = K, 
                                     history_file = res_history)

        #各サイクルの相図を出力
        nimsos.visualization.plot_phase_diagram.plot(input_file = candidates_file)



自作モジュールを利用する場合
==============================

.. code-block:: python

  import nimsos

  #目的関数の数を指定します．
  ObjectivesNum = 2

  #一度のサイクルで人工知能が提案する条件数を指定します．
  ProposalsNum = 2

  #サイクル数を指定します．
  CyclesNum = 3


  #実験条件をリスト化したファイルを指定
  candidates_file = "./candidates.csv"

  #人工知能が提案する条件を記載するファイルを指定
  proposals_file = "./proposals.csv"


  #ロボット実験における入力ファイルを格納するフォルダを指定
  input_folder = "./EXPInput"

  #ロボット実験からの出力ファイルを格納するフォルダを指定
  output_folder = "./EXPOutput"


  #履歴を格納するリストを作成
  res_history = nimsos.history(input_file = candidates_file, num_objectives = ObjectivesNum)

  for K in range(CyclesNum):

      print("Start cycle", K+1)


      #人工知能の実行
      import ai_tool_original
      ai_tool_original.ORIGINAL(input_file = candidates_file,
                                output_file = proposals_file,
                                num_objectives = ObjectivesNum,
                                num_proposals = ProposalsNum).select()
    

      #ロボット実験用インプットファイルの作成およびロボット実験の実行
      import preparation_input_original
      preparation_input_original.ORIGINAL(input_file = proposals_file, 
                                          input_folder = input_folder).perform()


      #ロボット実験結果の解析と実験条件ファイルの更新
      import analysis_output_original
      analysis_output_original.ORIGINAL(input_file = proposals_file, 
                                        output_file = candidates_file,
                                        num_objectives = ObjectivesNum, 
                                        output_folder = output_folder).perform()

      #履歴を格納するリストを更新
      res_history = nimsos.history(input_file = candidates_file, num_objectives = ObjectivesNum, itt = K, history_file = res_history)

      #各サイクルの目的関数のデータ分布を出力
      nimsos.visualization.plot_distribution.plot(input_file = candidates_file, num_objectives = ObjectivesNum)


  #目的関数のサイクル依存性をプロット
  nimsos.visualization.plot_history.cycle(input_file = res_history, num_cycles = CyclesNum)

  #目的関数の最大値のサイクル依存性をプロット
  nimsos.visualization.plot_history.best(input_file = res_history, num_cycles = CyclesNum)
