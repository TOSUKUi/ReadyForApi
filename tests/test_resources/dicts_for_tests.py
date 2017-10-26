from datetime import datetime

project_text = """
              <h2 class="u-d_none">プロジェクト概要</h2>
                <a class="button-link" href="/projects/solarboat/accomplish_report">
                  <div class="AccomplishReport-button">
                    <span>
                      <i class="fa fa-exclamation-circle" aria-hidden="true"></i>
                      プロジェクトの終了が報告されました
                      <i class="fa fa-angle-right" aria-hidden="true"></i>
                    </span>
                  </div>
</a>              <p><span style="font-family:times new roman,times,serif;">&nbsp;</span></p>

<div style="padding: 15px 5px; border-radius: 1px; border: 1px solid rgb(217, 166, 46); font-size: 12px; margin-right: 5px; margin-left: 5px; background-color: rgb(255, 255, 255);">
<p><span style="font-size:16px;"><span style="font-family:times new roman,times,serif;"><strong>【プロジェクト終了まで残り31日、無謀かもしれませんが、みなさまの応援に励まされ、もう一度目標を設定することを決めました】</strong><br />
<br />
先日、4月7日よりスタートした、クラウドファンディングのプロジェクトが、無事目標額2,000万円に到達したことをご報告いたしましたが、達成することが出来たのは、皆様のおかげです。本当にありがとうございました。<br />
<br />
実はこの太陽の船発掘・修復・保存・復原の全工程を達成させるためにはまだまだ多くの課題が残っています。その多くは技術面というよりは、資金面です。</span></span></p>

<p>&nbsp;</p>

<p><span style="font-size:16px;"><span style="font-family:times new roman,times,serif;">完全に復原するためにはあと3億円はかかる予定です。2年後には部材の発掘・修復・保存処理（ここまでの資金の目途はたっております）が終了します。</span></span></p>

<p>&nbsp;</p>

<p><span style="font-size:16px;"><span style="font-family:times new roman,times,serif;">この間に皆様からの当初のご支援でコンピュータ上に3D想定復原図を作ります。</span></span></p>

<p>&nbsp;</p>

<p><span style="font-size:16px;"><span style="font-family:times new roman,times,serif;">そしていよいよ復原ということになるのですが、その復原の為にはまずはプラスティックの実物大模型を作る必要があります。まずその模型に取り上げた部材を張り付け、形として完成させ、その後それを実際の姿に復原するのです。</span></span></p>

<p>&nbsp;</p>

<p><span style="font-size:16px;"><span style="font-family:times new roman,times,serif;">スタート時点は、みなさまにどのくらい応援していただけるのか、正直不安なこともあり、まずは3Dスキャナーの購入費のみに絞り、プロジェクトをはじめました。</span></span></p>

<p>&nbsp;</p>

<p><span style="font-size:16px;"><span style="font-family:times new roman,times,serif;">しかし、みなさまの温かい応援のおかげで、早めにこちらの資金が集まったこともあり、もしかすると残された31日で次のステップもやれるのではないかと期待を膨らませています。<br />
<br />
太陽の船の復原とピラミッド王墓説を覆すということは、私の人生をかけた最後にして最大の挑戦で、全財産をなげうってでも挑もうと、いまはアパート暮らしです。それくらい本気です。</span></span></p>

<p>&nbsp;</p>

<p><span style="font-size:16px;"><span style="font-family:times new roman,times,serif;">もう一度目標を設定するにあたり、この数日とても悩みました。</span></span></p>

<p><span style="font-size:16px;"><span style="font-family:times new roman,times,serif;">それでもあと少し、もう少しだけ、みなさまのお力をお借りできないかと思い、本日再スタートを切った次第です。</span></span></p>

<p>&nbsp;</p>

<p><span style="font-size:16px;"><span style="font-family:times new roman,times,serif;">残り31日であと2000万円、無謀な挑戦かもしれませんが、人生最後にして最大の挑戦をどうか応援していただけないでしょうか。</span></span></p>

<p>&nbsp;</p>

<p><span style="font-size:16px;"><span style="font-family:times new roman,times,serif;">皆様からのご厚意への感謝と再びお願いする無礼をお許し下さい。</span></span></p>

<p><span style="font-size:16px;"><span style="font-family:times new roman,times,serif;">ぜひご支援よろしくお願い申し上げます。</span></span></p>

<p>&nbsp;</p>

<p style="text-align: right;"><span style="font-size:16px;"><span style="font-family:times new roman,times,serif;">2017年5月30日追記</span></span></p>
</div>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p><span style="font-family:times new roman,times,serif;">▼以下もぜひご覧ください</span></p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<div style="padding: 10px 15px; text-align: center; font-size: 16px; margin-top: 15px; margin-bottom: 10px; border-top-color: rgb(217, 166, 46); border-bottom-color: rgb(217, 166, 46); border-top-width: 2px; border-bottom-width: 2px; border-top-style: solid; border-bottom-style: solid;"><span style="font-size: 16px;"><span style="font-family: times new roman,times,serif;"><strong>&mdash; 第2の太陽の船発見から30年 &mdash;</strong></span></span><br />
<br />
<span style="font-size: 16px;"><span style="font-family: times new roman,times,serif;"><strong>幼いころ夢見たその地で、<br />
「歴史を変える」<br />
その瞬間を信じて突き進む！</strong></span></span></div>

<p>&nbsp;</p>

<div style="padding: 15px 5px; border-radius: 1px; border: 1px solid rgb(217, 166, 46); font-size: 12px; margin-right: 5px; margin-left: 5px; background-color: rgb(255, 255, 255);">
<p style="text-align: center;"><span style="font-size: 16px;"><span style="font-family: times new roman,times,serif;"><strong>エジプト考古学研究者人生をかけた<br />
最後にして最大の挑戦へ</strong></span></span></p>
</div>

<p>&nbsp;</p>

<p>&nbsp;</p>

<div style="padding: 7px; border-bottom-color: rgb(217, 166, 46); border-left-color: rgb(217, 166, 46); border-bottom-width: 1px; border-left-width: 10px; border-bottom-style: solid; border-left-style: solid;"><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;"><strong>長年の夢、ピラミッド建造の目的解明を目指して。鍵を握るは「太陽の船」</strong></span></span></div>

<p>&nbsp;</p>

<p><span style="font-family: georgia,serif;"><span style="font-size: 16px;"><strong><span style="color: rgb(217, 166, 46);"><span style="background-color: rgb(217, 166, 46);">□</span>&nbsp;</span></strong></span></span><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;"><strong>30年前、我々が発見した第2の太陽の船を4550年の永い眠りから解き放ち、当時の姿へ甦らせたい！</strong></span></span></p>

<p>&nbsp;</p>

<p><span style="display: none;">&nbsp;</span><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">みなさんこんにちは、吉村作治です。私とエジプトとの出会いは、幼い頃</span></span><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">ツタンカーメンの墓を見つけたイギリス人考古学者「ハワード・カーター」の伝記を読んだことがはじまりです。</span></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">その後エジプトへ憧憬の念を抱き、</span></span><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">研究者への道を志すようになりました。</span></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">念願叶って、大学生の頃に初めて現地調査を行って以降は、現在まで半世紀以上に渡り、エジプト研究を続けています。</span></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;"><span contenteditable="false" tabindex="-1"><img alt="" data-widget="image" height="382" src="https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/236526/content_c2ca448d931523f898d4b4a229dc0f3833b087fe.png" width="610" /></span></span></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">しかし、我が研究人生の中で、あともう少しのところで、いまだ解き明かすことができていない謎があります。</span></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">それが、</span></span><strong><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">「ピラミッド建造の目的」</span></span></strong><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">です。</span></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">​<span contenteditable="false" tabindex="-1"><img alt="" data-widget="image" height="407" src="https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/233997/content_dcdfd41cb6e96e78736deb5f5add6f6311da8e80." width="610" /></span></span></span></p>

<p>&nbsp;</p>

<p><strong><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">定説では「ピラミッドは王の墓である」とされていますが、私は長期に渡る研究から、この説は成り立たないと考えています。</span></span></strong></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;">しかし<span style="font-size: 16px;">物証が少なく、いまだピラミッド王墓説を完全に覆すまでには至っていません。</span></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">で<span style="display: none;">&nbsp;</span>すが私ももう74歳、あとどのくらい時間があるか正直分かりません。</span><span style="display: none;">&nbsp;</span></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">そこで、長年の夢を何とか果たすべく、<strong><u>ピラミッド建造の目的を解き明かす鍵を握る「第2の太陽の船」のより早い完全修復と復原を目指し</u>、</strong>今回プロジェクトを立ち上げました。</span></span></p>

<p>&nbsp;</p>

<p><strong><span style="font-family: times new roman,times,serif;">この壮大な挑戦をどうかみなさま応援していただけないでしょうか。よろしくお願いいたします。</span></strong></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;"><span contenteditable="false" tabindex="-1"><img alt="" data-widget="image" height="462" src="https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/236535/content_45561166ea69349fd80b224b1dfbeaa50eb7ee2d.jpg" width="610" /></span></span></span></p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<div style="padding: 7px; border-bottom-color: rgb(217, 166, 46); border-left-color: rgb(217, 166, 46); border-bottom-width: 1px; border-left-width: 10px; border-bottom-style: solid; border-left-style: solid;"><span style="font-family: times new roman,times,serif;"><strong>広大な</strong></span><span style="font-family: times new roman,times,serif;"><strong>砂漠の中に存在する「船」</strong></span></div>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;"><strong><span style="color: rgb(217, 166, 46);"><span style="background-color: rgb(217, 166, 46);">□</span>&nbsp;</span>ナイル川の恩恵を受け発展した、古代エジプトならではの自然崇拝と死生観</strong></span></span><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;"><strong>が生み出した、</strong></span><strong><span style="font-size: 16px;">世界最古の大型木造船</span></strong><span style="font-size: 16px;"><strong>「太陽の船」とは？</strong></span></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">古代エジプトでは、「太陽が毎朝東の空からのぼって、西の空に沈んでいく、そして再び翌日東の空からのぼってくる」その姿に永遠の命を見いだし、生きとし生けるもの全てを育む存在として、崇拝していました。</span></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">その太陽を神格化したのが太陽神「ラー」であり、毎日太陽が昇り降りするのは、太陽神「ラー」が船に乗り、大空を航海しているからと考えられていました。</span></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">また王の死後は、その魂はラーと共に永遠の航海にでるとも考えられていたのです。</span></span></p>

<p>&nbsp;</p>

<p><img alt="" height="467" src="https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/237598/content_dcdfd41cb6e96e78736deb5f5add6f6311da8e80." width="610" /></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">さらに「エジプトはナイルの賜物」という言葉があるように、ナイル川の恩恵を受け発展をしていた当時、「船」は長距離の移動に使う需要な交通手段でした。</span></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">そのため、「あの世」と「この世」という、果てしなく永い距離を移動するために、現世同様、「船」が用意されたと考えられています。それが「太陽の船」です。</span></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span contenteditable="false" tabindex="-1"><img alt="" data-widget="image" height="431" src="https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/236618/content_dcdfd41cb6e96e78736deb5f5add6f6311da8e80." width="610" /></span></span></p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<div style="padding: 7px; border-bottom-color: rgb(217, 166, 46); border-left-color: rgb(217, 166, 46); border-bottom-width: 1px; border-left-width: 10px; border-bottom-style: solid; border-left-style: solid;"><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;"><strong>二隻存在する太陽の船。研究を重ねていくなかで、それぞれ異なった役割を持っていることが分かってきています。</strong></span></span></div>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;"><strong><span style="color: rgb(217, 166, 46);"><span style="background-color: rgb(217, 166, 46);">□</span>&nbsp;</span>&nbsp;30年前に、我々が科学の力をもって、クフ王のピラミッドの南側で発見したのは「第2の太陽の船」です。</strong></span></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">二隻ある太陽の船のうち、一隻は1954年にエジプト人の手により発見され、当時の姿へと復原されています。全長43メートルあるその船は、現在ギザの博物館に展示されています。</span></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;">実は第1の船発見当時、西側にももう一隻太陽の船があると言われていましたが、発見はされていませんでした。</span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;">そんな中、第1の船一般公開後、各国が「第2の船」へのアプローチを開始し、</span><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">我々の調査隊も、電磁波探査レーダーによる非破壊検査を実施しました。</span></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">そしてついに、船坑（船の部材を収納するための地面にあけられた穴）内に木材と見られる反応を見つけ、幻であった第2の船の存在をつきとめることができたのです。</span></span></p>

<p>&nbsp;</p>

<p><img alt="" height="407" src="https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/237646/content_c2ca448d931523f898d4b4a229dc0f3833b087fe.png" width="610" /></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;"><strong><span style="color: rgb(217, 166, 46);"><span style="background-color: rgb(217, 166, 46);">□</span>&nbsp;</span>&nbsp;</strong></span></span><strong><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">当初二隻の船は、王と神が乗った</span>「昼の船」「夜の船」もしくは「この世の船」「あの世の船」と考えられ、<span style="font-size: 16px;">同一の目的のために使用されたと考えられていました。</span></span></strong></p>

<p><br />
<span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">しかし発見後、全体の2/3まで発掘・修復作業が進むうち、二隻にはいくつもの違いが見えてきたのです。</span></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;">大きな違いとしては、</span></p>

<p><strong><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">①第1の船と第2の船で発見されたオールの長さが異なる点</span></span></strong></p>

<p><strong><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">②第2の船にのみ、大量の金属製の金具が使用されていた点</span></span></strong></p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;"><strong>③第2の船にのみ、帆柱と思われるような部材、また第1の船より多くの布や縄が見つかっている点</strong>　の３点があります。</span></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">第1の船からは漕ぐ目的で使用するには長すぎるオールのみが、第2の船からは第1の船と同じ長いオールと、その半分以下の長さの短く漕ぐのに最適な長さのオールが見つかっています。</span></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">そして、第2の船でのみ出土した金属製の金具は、王墓の壁画等に残された、「太陽の船」建造時の様子と照らし合わせてみても、オールを取り付ける部位だと考えられます。</span></span></p>

<p>&nbsp;</p>

<p><img alt="" height="406" src="https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/237599/content_c2ca448d931523f898d4b4a229dc0f3833b087fe.png" width="610" /></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">また同じく第2の船からのみ出土している布は「帆」であり、柱は「帆柱」、縄は二つの船を結びつけるものだと推測され、現在発掘している第2の太陽の船は、動力船であったと考えられるのです。</span></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">これらから、我々は、役割の異なった「太陽神ラーと王を乗せた第1の船」と「動力船であった第2の船」はロープで繋がれ、ともに大空を航行するために造られたと考えています。</span></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">もちろん、第2の船の研究を進めるまでは、私自身も多くの研究者が残してきた定説を信じてきました。</span></span><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">しかし、<u>時に自分の研究が歴史を変えることもあること</u>を身をもって体験したのです。</span></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">だからこそ、私はこの船を修復・復原することは、これまでの歴史を覆すほどの可能性を秘めていると信じています。</span></span></p>

<p>&nbsp;</p>

<p><img alt="" height="343" src="https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/237647/content_c2ca448d931523f898d4b4a229dc0f3833b087fe.png" width="610" /></p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<div style="padding: 7px; border-bottom-color: rgb(217, 166, 46); border-left-color: rgb(217, 166, 46); border-bottom-width: 1px; border-left-width: 10px; border-bottom-style: solid; border-left-style: solid;"><span style="font-family: times new roman,times,serif;"><strong>発見から30年、発掘・修復作業には</strong></span><strong style="font-family: &quot;times new roman&quot;, times, serif;">度重なる苦難がともない、ある人は「ピラミッドの呪いだ」とさえ言いました</strong><strong style="font-family: georgia, serif;">。</strong></div>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;"><strong><span style="color: rgb(217, 166, 46);"><span style="background-color: rgb(217, 166, 46);">□</span>&nbsp;</span></strong><strong>第2の船発見後、</strong></span><strong><span style="font-size: 16px;">バブル崩壊など日本の経済状況の悪化を受け、我々は発掘資金の調達が出来ぬまま、プロジェクトは休止状態に陥りました。</span></strong></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">スポンサー探しに奔走すること20年、ついに企業スポンサーがついて下さり、船坑をふさぐために並べられた蓋石の撤去作業が始まりました。</span></span><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">蓋石の重さは1枚あたり約13トン、これが40枚程がほぼ隙間なく並んでいる状態です。</span></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span contenteditable="false" tabindex="-1"><img alt="" data-widget="image" height="407" src="https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/236614/content_dcdfd41cb6e96e78736deb5f5add6f6311da8e80." width="610" /></span></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">しかし当時エジプト政府からは、発掘現場に重機を持ち込むことは禁止されていたため、</span>我々は<span style="font-size: 16px;">知恵を出し合い、発掘・修復作業を行う巨大なテントの組み立てから蓋石の撤去まで、自分たちの手で進めることとなったのです。</span></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">このとき活躍したのが、日本の伝統技術である「玉掛け法」です。</span></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;"><span contenteditable="false" tabindex="-1"><img alt="" data-widget="image" height="406" src="https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/236615/content_dcdfd41cb6e96e78736deb5f5add6f6311da8e80." width="610" /></span></span></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;"><strong><span style="color: rgb(217, 166, 46);"><span style="background-color: rgb(217, 166, 46);">□</span>&nbsp;</span></strong></span><strong><span style="font-size: 16px;">ようやく進み始めた最中、2011年アラブの春などの革命が起こり、またも発掘作業は一時中断せざるおえない状況になりました。</span></strong></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">再び窮地に立たされた我々ですが、「ここで諦めるわけにはいかない」と、いつか夜が明けることを信じて、ひたすらそのときを待ち続けました。</span></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">そして何とか無事作業は再開され、全ての蓋石を撤去することに成功したのです。ですが、作業の大幅な遅れにより、企業スポンサーさまからのご支援を頂く期間は終了を迎えてしまいました。</span></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span contenteditable="false" tabindex="-1"><img alt="" data-widget="image" height="458" src="https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/236611/content_dcdfd41cb6e96e78736deb5f5add6f6311da8e80." width="610" /></span></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">現在は、JICA(独立行政法人国際協力機構）や太陽の船サポーターの皆様に支えられ、自分たちの手で、深さ4メートルのところに埋まった木材を取り上げるためのゴンドラを組み立てたりしながら、発掘・修復作業を進めています。</span></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span contenteditable="false" tabindex="-1"><img alt="" data-widget="image" height="409" src="https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/236622/content_c2ca448d931523f898d4b4a229dc0f3833b087fe.png" width="610" /></span></span></p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<div style="padding: 7px; border-bottom-color: rgb(217, 166, 46); border-left-color: rgb(217, 166, 46); border-bottom-width: 1px; border-left-width: 10px; border-bottom-style: solid; border-left-style: solid;"><span style="font-family: times new roman,times,serif;"><strong>今のペースでは、残り1/3を発掘・修復し、復原に向けた3D図を作成するまでに、あと3年はかかることが予想されます。</strong></span></div>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;"><strong><span style="color: rgb(217, 166, 46);"><span style="background-color: rgb(217, 166, 46);">□</span>&nbsp;</span>長い間埋まっていた木材は、劣化が激しく、1本の木材がいくつにも割れ、歪んでしまっているため、保存・修復作業は難航を極めています。</strong></span></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">我々は、推定全長38メートルの木製のこの船を、永い眠りから解き放ち、当時の姿へ甦らせようと奮闘してきました。</span></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">しかし、一刻も早い作業完了が望まれる中、設計図もなく、かなり劣化した木材を元の姿に戻すためには、レーザースキャナーを使い三次元画像を作成し、変形した木材をＰＣ上で矯正し復原図を作成していくことが不可欠です。</span></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span contenteditable="false" tabindex="-1"><img alt="" data-widget="image" height="407" src="https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/236620/content_c2ca448d931523f898d4b4a229dc0f3833b087fe.png" width="610" /></span></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">その後、木片の歪みを修復し、保存するのですが、例えば、10メートルの木材であれば、全ての作業を終えるまでに、およそ3週間かかります。</span></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span contenteditable="false" tabindex="-1"><img alt="" data-widget="image" height="407" src="https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/236621/content_c2ca448d931523f898d4b4a229dc0f3833b087fe.png" width="610" /></span></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">それでも、最先端の科学を駆使し作られた保存剤と遺跡の修復に携わってきた職人技を組み合わせ、これまで何とか保存・修復作業を進め、全体のおよそ2/3まで作業は完了しました。</span></span></p>

<p>&nbsp;</p>

<p><img alt="" height="448" src="https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/237614/content_dcdfd41cb6e96e78736deb5f5add6f6311da8e80." width="610" /></p>

<p>&nbsp;</p>

<p><strong><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">しかし、残り1/3を完了するまでにあと３年程かかると予想されます。</span></span></strong></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">3D測量は、現在も東大の研究チームが進めていますが、我々は自前の機材を持ち合わせていないため、3D測量を行う時間が限られています。</span></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><u><span style="font-size: 16px;"><span style="background-color: rgb(250, 235, 215);">そこで今回、新たにレーザースキャナー等自前の機材を購入することにより、1年、復原図作成までの時間短縮を目指そうと考えています。</span></span></u></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">実際に第2の船を当時の姿に復原するには、復原図を元に組み立て作業を行うのにあと５年程かかり、すべての工程を遂行するのには、3億円程かかる壮大なプロジェクトになる予定です。</span></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">ですが、まずは3D測量を終え、PC上で復原図（組み立て時に用いる設計図）を作成することができなければ、復原を進めることもできず、新たな情報を得ることができません。</span></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">先のことを考えると、たった1年の短縮がと思われる方もいるかもしれません。</span></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">しかし、私のこの命があるうちに、</span></span><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">何としても「ピラミッド建造の目的」を解明し、「ピラミッド王墓説」を覆したい、そのために第2の太陽の船の発掘・修復作業を遂行する必要があるのです。</span></span></p>

<p>&nbsp;</p>

<p><img alt="" height="457" src="https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/237613/content_dcdfd41cb6e96e78736deb5f5add6f6311da8e80." width="610" /></p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<div style="padding: 7px; border-bottom-color: rgb(217, 166, 46); border-left-color: rgb(217, 166, 46); border-bottom-width: 1px; border-left-width: 10px; border-bottom-style: solid; border-left-style: solid;"><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;"><b>この挑戦を後押しするように、ついに昨年には、10年間に及ぶ交渉の末、エジプト政府からクフ王の墓発掘の許可をもらうことに成功しました！</b></span></span></div>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;"><strong><span style="color: rgb(218, 165, 32);"><span style="background-color: rgb(218, 165, 32);">□</span>&nbsp;</span>2016年、第2の太陽の船の修復作業と並行して、ついに、いまだ発見に至っていない「クフ王の墓」の探索がはじまりました。</strong></span></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">エジプトでは、数多くのピラミッドが見つかっていますが、中からは、ミイラや副葬品の欠片さえ見つかっていません。</span></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">そして、一人の王が複数のピラミッドを建造しているケースが多いことから、やはり「ピラミッドは王の墓である」という説は成り立たないと思われます。</span></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><strong><span style="font-size: 16px;">ただ物証が少ないため、我々はピラミッド王墓説を完全に覆すまでには至っていません。</span></strong></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><strong><span style="font-size: 16px;"><img alt="" height="407" src="https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/237615/content_5d114bc8e3c1fb8b1af736cdd793c3b8952ec315.jpg" width="610" /></span></strong></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">しかし、2016年4月よりついに、新たに「クフ王墓探査プロジェクト」を開始することができました！ピラミッドの外から王墓が実際に発見されれば、それこそピラミッドは王の墓ではないという説の物証となります。</span></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;">第2の太陽の船を発掘・修復作業で新たに見つけた情報は、クフ王の墓を見つけるヒントにもなっているのです。</span></p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<div style="padding: 7px; border-bottom-color: rgb(217, 166, 46); border-left-color: rgb(217, 166, 46); border-bottom-width: 1px; border-left-width: 10px; border-bottom-style: solid; border-left-style: solid;"><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;"><strong>しかし、なぜ日本人の私が、1万キロ以上も離れたエジプトの地で研究を続けるか？と思われる方もいらっしゃるかもしれません。</strong></span></span></div>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;"><strong><span style="color: rgb(217, 166, 46);"><span style="background-color: rgb(217, 166, 46);">□</span>&nbsp;</span></strong></span><span style="font-size: 16px;"><strong>実は、我々日本と古代エジプトには数多くの共通点が存在し、それらは「ピラミッド建造の目的」を解き明かす道しるべとなるのです。</strong></span></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">太陽神ラー同様「自然崇拝」の考えは、3000年の時を経て、シルクロードを通じ、日本にも伝わっていました。その一つが、日本の大阪府交野市にある磐船神社に存在します。</span></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">日本の代表的な太陽神でもある、天照大神の孫が祀られていると言われているこの神社には、神様が天から地上に降臨される際に、「天の磐船」と呼ばれる、船にお乗りになっていたという言い伝えがあるのです。</span></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">日本各地のお祭りも自然崇拝に所以があるものの一つです。</span></span></p>

<p>&nbsp;</p>

<p><img alt="" height="458" src="https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/237651/content_dcdfd41cb6e96e78736deb5f5add6f6311da8e80." width="610" /></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;"><strong><span style="color: rgb(217, 166, 46);"><span style="background-color: rgb(217, 166, 46);">□</span>&nbsp;</span>さらに日本の阿弥陀如来は、私に「黄金＝権力の象徴ではない」という考えを与えてくれました。</strong></span></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">古代エジプトの貴族の墓には、死者があの世で、苦しみや悩みから救われ、何不自由のない生活が送れるようにと、壁画に太陽神ラーとラーのもとで、光に満ちあふれ、苦しみや悩みから救われる来世の様子が描かれていました。</span></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">一方日本では、毎年お盆の時期に、死者の霊をあの世へと送り届けるために、京都府京都市左京区にある如意ヶ嶽で、「京都五山の送り火」が行われます。</span></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">ここでは、大文字焼きに加え、実は山肌に西の方角を向いた「舟形」が打ち出され、死者の霊を西方極楽浄土に送り届ける役割を果たしています。</span></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">西方極楽浄土とは、阿弥陀如来がいる世界、すなわち「苦しみや悩みから救われ、何も不自由がない世界」のことを指します。</span></span></p>

<p>&nbsp;</p>

<p><u><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">共に黄金に光り輝き、「苦しみや悩みから救われ、何も不自由がない世界」を作り出す、太陽神ラーと阿弥陀如来。</span></span></u></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">この繋がりを発見したとき、我々は、ピラミッドに埋蔵される数々の黄金の品は、「王があの世で、苦しみや悩みから救われ、何も不自由がない生活を送れるように」という願いが込められたものなのではないかと考えるようになりました。</span></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;">このように密接に関わり合う古代エジプトと日本。この二つが繋がったとき、ピラミッドの謎解明に向けた扉が開くのやもしれません。</span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;">これまで私が日本人でありながらも、<span style="font-size: 16px;">エジプト考古学者として歩んでこれたのには、こうした背景があるのです。</span></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">さまざまな想いを持ちながら歩んできたエジプト考古学者としての道のり、その集大成として「ピラミッド建造の目的解明」を成し遂げたい。</span></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">この最後にして最大の挑戦に、全財産をなげうってでも挑もうと、いまはアパート暮らしです。それくらい本気です。</span></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><strong><span style="font-size: 16px;">みなさま、</span></strong><strong><span style="font-size: 16px;">どうか私に力を貸していただけないでしょうか。そして、この挑戦を応援する仲間になっていただけないでしょうか。</span></strong></span><span style="font-family: times new roman,times,serif;"><strong>応援どうぞよろしくお願いいたします。</strong></span></p>

<p>&nbsp;</p>

<p><img alt="" height="435" src="https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/237611/content_b629b7dc02fe6f5723da7d5f3dd63eb28fb5f3e4.jpg" width="610" /></p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<div style="padding: 7px; border-bottom-color: rgb(217, 166, 46); border-left-color: rgb(217, 166, 46); border-bottom-width: 1px; border-left-width: 10px; border-bottom-style: solid; border-left-style: solid;"><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;"><b>本プロジェクトについて　※注意点※</b></span></span></div>

<p>&nbsp;</p>

<p><strong><span style="font-family: times new roman,times,serif;">※1※</span></strong></p>

<p><span style="font-family: times new roman,times,serif;">第2の船、発掘・保存・修復にかかる年月は、これから最短で2年と見積もっておりますが、現場では予期せぬことが発生することもあり、その場合は作業の一時中断や大幅な遅延が発生する可能性もございます。</span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;">その場合には、新着情報の中でお知らせをいたしますが、不慮の事態が発生する可能性がありますこと、あらかじめご理解いただけますと幸いです。</span></p>

<p>&nbsp;</p>

<p><strong><span style="font-family: times new roman,times,serif;">※2※</span></strong></p>

<p><span style="font-family: times new roman,times,serif;">また、今回記載しておりますのは、あくまで現時点での見解であり、今後研究が進む中で、異なった見解が生まれる可能性もございますこと、重ねてご理解いただけますと幸いです。</span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><strong>※3※</strong></span></p>

<p><span style="font-family:times new roman,times,serif;">今回は、リターンの発送の兼ね合いから、日本国内在住の方のみご支援可能となります。何卒ご了承ください。</span></p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<div style="padding: 7px; border-bottom-color: rgb(217, 166, 46); border-left-color: rgb(217, 166, 46); border-bottom-width: 1px; border-left-width: 10px; border-bottom-style: solid; border-left-style: solid;"><span style="font-family:times new roman,times,serif;"><b>支援金の使途について</b></span></div>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">今回集まった資金は、太陽の船復原に向けた、復原図作成のために必要な3D測量を行う、レーザースキャナー等自前の機材を購入することに充てさせていただきます。</span></span></p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<div style="padding: 7px; border-bottom-color: rgb(217, 166, 46); border-left-color: rgb(217, 166, 46); border-bottom-width: 1px; border-left-width: 10px; border-bottom-style: solid; border-left-style: solid;"><span style="font-family: times new roman,times,serif;"><b>プロジェクトメンバーとプロジェクトにかける思いについて</b></span></div>

<p>&nbsp;</p>

<p><span style="font-size: 16px;"><span style="font-family: times new roman,times,serif;"><strong>◆現場主任：黒河内 宏昌<br />
（東日本国際大学 エジプト考古学研究所 客員教授）</strong></span></span></p>

<div style="padding: 15px 5px; border-radius: 1px; border: 1px solid rgb(217, 166, 46); font-size: 12px; margin-right: 5px; margin-left: 5px; background-color: rgb(255, 255, 255);">
<p><img alt="" height="200" src="https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/237600/content_339f5868588cfc8fda4a1ec94ead8f737c5fcfc0." width="150" /></p>

<p>&nbsp;</p>

<p><span style="font-size: 16px;"><span style="font-family: times new roman,times,serif;">太陽の船プロジェクトは、分解された木造船の1200点にも及ぶ部材を地中のピットから取り上げ、保存処理を施し、三次元測量データをもとにした復原考察ののち、組み立て復原することを目的としています。現場主任として参加できることを大変ありがたく思っています。</span></span></p>
</div>

<p>&nbsp;</p>

<p><strong><span style="font-family: times new roman,times,serif;">◆取り上げ発掘担当：高橋 寿光<br />
（東日本国際大学 エジプト考古学研究所 客員講師）</span></strong></p>

<div style="padding: 15px 5px; border-radius: 1px; border: 1px solid rgb(217, 166, 46); font-size: 12px; margin-right: 5px; margin-left: 5px; background-color: rgb(255, 255, 255);">
<p><span style="font-family: times new roman,times,serif;"><img alt="" height="201" src="https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/237601/content_339f5868588cfc8fda4a1ec94ead8f737c5fcfc0." width="150" /></span></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">私は太陽の船の木製部材を一つ一つ、地中のピットから取り上げる仕事に毎日たずさわっています。ピットの中の出土状況も三次元測量する必要があります。プロジェクトへのご協力をよろしくお願いいたします。</span></span></p>
</div>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;"><strong>◆取り上げ発掘担当：マムドゥーフ・ターハ（Mamdoh Taha）</strong></span></span></p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;"><strong>(エジプト考古省、太陽の船プロジェクト チーフアーケオロジスト）</strong></span></span></p>

<div style="padding: 15px 5px; border-radius: 1px; border: 1px solid rgb(217, 166, 46); font-size: 12px; margin-right: 5px; margin-left: 5px; background-color: rgb(255, 255, 255);">
<p><img alt="" height="200" src="https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/237602/content_339f5868588cfc8fda4a1ec94ead8f737c5fcfc0." width="150" /></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">エジプト人にとってクフ王は「おじいさん」のような存在です。そのクフ王の太陽の船を、三次元測量をもとにした精密な復原考察により組み立てるプロジェクトに参加できることを、大変光栄に思います。</span></span></p>
</div>

<p>&nbsp;</p>

<p><strong><span style="font-size: 16px;"><span style="font-family: times new roman,times,serif;">◆保存修復担当：アイーサ・ジダン（Eissa Zidan）<br />
（エジプト考古省、大エジプト博物館保存修復センター ダイレクター太陽の船プロジェクト チーフコンサベーター）</span></span></strong></p>

<div style="padding: 15px 5px; border-radius: 1px; border: 1px solid rgb(217, 166, 46); font-size: 12px; margin-right: 5px; margin-left: 5px; background-color: rgb(255, 255, 255);">
<p><img alt="" height="200" src="https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/237603/content_339f5868588cfc8fda4a1ec94ead8f737c5fcfc0." width="150" /></p>

<p>&nbsp;</p>

<p><span style="font-size: 16px;"><span style="font-family: times new roman,times,serif;">太陽の船の部材を保存処理することが私の仕事です。そして現在建設中の世界最大の大エジプト博物館で、組み立て復原ののちに展示するプロジェクトを日本と共同でできることを、大変うれしく思います。</span></span></p>
</div>

<p>&nbsp;</p>

<p><strong><span style="font-size: 16px;"><span style="font-family: times new roman,times,serif;">◆保存修復担当：西坂 朗子<br />
（東日本国際大学 エジプト考古学研究所 客員准教授）</span></span></strong></p>

<div style="padding: 15px 5px; border-radius: 1px; border: 1px solid rgb(217, 166, 46); font-size: 12px; margin-right: 5px; margin-left: 5px; background-color: rgb(255, 255, 255);">
<p><img alt="" height="201" src="https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/237604/content_339f5868588cfc8fda4a1ec94ead8f737c5fcfc0." width="150" /></p>

<p>&nbsp;</p>

<p><span style="font-size: 16px;"><span style="font-family: times new roman,times,serif;">ピラミッドの時代から地中に眠っていた、謂わば「タイムカプセル」から船を取り上げるというこの壮大なプロジェクトに携わることができて大変光栄です。根気のいる作業ですが、一点、一点の木材を大切に、慎重に、修復処置を行っていきたいと思います。</span></span></p>
</div>

<p>&nbsp;</p>

<p><span style="font-size: 16px;"><span style="font-family: times new roman,times,serif;"><strong>◆保存修復担当：吉村 佳南<br />
（太陽の船プロジェクト コンサベーター）</strong></span></span></p>

<div style="padding: 15px 5px; border-radius: 1px; border: 1px solid rgb(217, 166, 46); font-size: 12px; margin-right: 5px; margin-left: 5px; background-color: rgb(255, 255, 255);">
<p><img alt="" height="200" src="https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/237605/content_339f5868588cfc8fda4a1ec94ead8f737c5fcfc0." width="150" /></p>

<p>&nbsp;</p>

<p><span style="font-size: 16px;"><span style="font-family: times new roman,times,serif;">太陽の船の木製部材を保存処理することは、とても面白く、また奥の深い作業です。私はたくさんの仲間たちとともにこれをやり遂げることに、人生をかけて頑張るつもりです。</span></span></p>
</div>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;"><strong>◆三次元測量担当：大石 岳史<br />
（東京大学 生産技術研究所 准教授）</strong></span></span></p>

<div style="padding: 15px 5px; border-radius: 1px; border: 1px solid rgb(217, 166, 46); font-size: 12px; margin-right: 5px; margin-left: 5px; background-color: rgb(255, 255, 255);">
<p><img alt="" height="198" src="https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/237606/content_339f5868588cfc8fda4a1ec94ead8f737c5fcfc0." width="150" /></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">これまで培ったデジタルアーカイブ・形状解析技術を活用して本プロジェクトに貢献するとともに、情報技術を駆使して歴史的背景や当時の製造技術といった新たな知見が得られるよう研究を進めたいと考えています。</span></span></p>
</div>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;"><strong>◆三次元測量担当：影沢 政隆<br />
（東京大学 生産技術研究所 助教）</strong></span></span></p>

<div style="padding: 15px 5px; border-radius: 1px; border: 1px solid rgb(217, 166, 46); font-size: 12px; margin-right: 5px; margin-left: 5px; background-color: rgb(255, 255, 255);">
<p><img alt="" height="203" src="https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/237607/content_339f5868588cfc8fda4a1ec94ead8f737c5fcfc0." width="150" /></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">すべての部材を３次元計測しCGによる仮想復原の担当しています。共用計測装置を日本から毎回一時輸入しているため作業効率が悪い上、その一時輸入も困難になり、専用機の現地導入を切望する次第です。</span></span></p>
</div>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;"><strong>◆マネージメント担当：吉村 龍人<br />
（東日本国際大学 エジプト考古学研究所 カイロ事務所長）</strong></span></span></p>

<div style="padding: 15px 5px; border-radius: 1px; border: 1px solid rgb(217, 166, 46); font-size: 12px; margin-right: 5px; margin-left: 5px; background-color: rgb(255, 255, 255);">
<p><img alt="" height="200" src="https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/237608/content_339f5868588cfc8fda4a1ec94ead8f737c5fcfc0." width="150" /></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">太陽の船は世界最古の比類ない大型木造船です。これを発掘、保存修復、組み立て復原するプロジェクトは、大変ユニークな考古事業です。現地でのコーディネーションを全力でがんばります。</span></span></p>
</div>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;"><strong>◆マネージメント担当：ムハンマド・アシュリー（Mohamed Ashry）<br />
（東日本国際大学 エジプト考古学研究所 カイロ事務所 コーディネーター）</strong></span></span></p>

<div style="padding: 15px 5px; border-radius: 1px; border: 1px solid rgb(217, 166, 46); font-size: 12px; margin-right: 5px; margin-left: 5px; background-color: rgb(255, 255, 255);">
<p><img alt="" height="201" src="https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/237609/content_339f5868588cfc8fda4a1ec94ead8f737c5fcfc0." width="150" /></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">エジプトはあらゆる手続きに大変時間のかかる国です。世界に例のないこの太陽の船プロジェクトを成功させるため、私は粘り強く手続きの処理に取り組んでいきます。</span></span></p>
</div>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;"><strong>◆マネージメント担当：ユセフ・ナバラウィ（Youssef Nabarawy）<br />
（太陽の船プロジェクト エンジニア）</strong></span></span></p>

<div style="padding: 15px 5px; border-radius: 1px; border: 1px solid rgb(217, 166, 46); font-size: 12px; margin-right: 5px; margin-left: 5px; background-color: rgb(255, 255, 255);">
<p><img alt="" height="200" src="https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/237610/content_339f5868588cfc8fda4a1ec94ead8f737c5fcfc0." width="150" /></p>

<p>&nbsp;</p>

<p><span style="font-family: times new roman,times,serif;"><span style="font-size: 16px;">プロジェクトは全体的に見れば順調に進んでいますが、技術的な面ではまだまだ課題もあります。私はそれを解決するために、これからも努力していきます。</span></span></p>
</div>

<p>&nbsp;</p>

<p><strong><span style="font-family:times new roman,times,serif;">◆ご協力：考古大臣Khaled El-Enany博士</span></strong></p>

<p>&nbsp;</p>

<p>&nbsp;</p>


            </section>
            <!-- /概要 -->
            <hr>
            <section class="Project-update Tab__content">
                <h2>最新の新着情報</h2>
                <aside class="Project-update__related">
                  <article class="Project-update__related-item Media">
  <div class="Project-update__related-item-img Media__img">
    <a href="/projects/solarboat/announcements/64227">
      <img src="https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/274203/thumb_c6749bf1fd05837bb38a2d3c7ee5631cec5a9ffa.jpg" alt="Thumb c6749bf1fd05837bb38a2d3c7ee5631cec5a9ffa" width="120" height="120" />
</a>  </div>
  <div class="Project-update__related-item-main Media__body docs-area">
    <header class="Project-update__related-item-header">


        <time datetime="2017-10-03" class="Project-update__related-item-header-date">2017年10月03日</time>


      <h3 class="Project-update__related-item-header-h">
        <a class="u-font_b" href="/projects/solarboat/announcements/64227">現場からのレポート　現場の風景　その１</a>
      </h3>




    </header>
    <div  class="Project-update__related-item-body">
      <p>皆さまこんにちは。カイロの発掘現場にいる黒河内です。 このレポートでは何枚かの写真を使って、皆さまに実際に現場を訪れたような気分を味わっていただきたいと思います。今回は「その１」、では早速参りましょう。ここはカイロ郊外にある、エジプトで最も有名な遺跡の一つ、ギザのピラミッド地区で...</p>
    </div>
    <footer class="Project-update__related-item-footer">
      <a href="/projects/solarboat/announcements/64227">続きを見る</a>
    </footer>
  </div>
</article>

                """





project_summary_dict = {
    "project": {
        'id': 12194,
        'title': '人生最後の挑戦！ピラミッドの謎解明の鍵を握る太陽の船復原へ！',
        'image': 'https://readyfor.jp/s3/readyfor-img/project_photos/12194/medium/5b067a704b388146d7cd69be634c3c06b7286aa5.JPG?1491513707',
        'funded_percent': 161,
        'label_type': 'is-achieved',
        'user': {'name': '吉村作治（NPO法人太陽の船復原研究所所長）',
        'description': 'NPO法人太陽の船復原研究所\u3000所長。エジプト考古学者（工学博士）。',
        'my_image_url': 'https://readyfor.jp/s3/readyfor-img/user_images/269607/medium/4fc4b9d7c93013650208f752ec0b378f28883144.JPG?1495778978'},
        'user_twitter_link_url': None,
        'user_facebook_link_url': None,
        'user_other_link_url': None,
        'user_other_link_text': None,
        'user_profile_url': 'https://readyfor.jp/users/269607',
        'keyword': 'solarboat',
        'amount': '32,265,000',
        'is_expired': '終了日',
        'resize': 'https://readyfor.jp/assets/smartphone/common/resize_img400x300-3de11e3fef05756dc2789f3f6fc65ea617b93b784f220b11dac6d36fdbadfeb6.png',
        'matching': False,
        'is_matching_complete': False,
        'keep_it_all': False,
        'anticipative_amount': None,
        'is_accomplish_report_published': True,
        'user_signed_in': False,
        'user_watched': False,
        'not_watch_project_path': '/projects/solarboat/not_watch',
        'watchlists_count': 96,
        'watch_project_path': '/projects/solarboat/watch',
        'project_type': 'normal',
        'project_type_i18n': '購入型',
        'funding_model': 'all_or_nothing',
        'funding_model_i18n': 'All or Nothing',
        'backing_project_condition': None,
        'matching_banner_image': 'https://readyfor.jp/images/matching_gift/none/project_banner.jpg',
        'tags': [{'id': 116,
        'keyword': 'challenge',
        'name': 'チャレンジ',
        'desc': '',
        'image_file_name': 'challenge_TEAM_MARU.jpg',
        'image_content_type': 'image/jpeg',
        'image_file_size': 294407,
        'image_updated_at': '2016-10-12T19:13:04.000+09:00',
        'created_at': '2016-10-12T18:04:00.000+09:00',
        'updated_at': '2016-10-12T19:13:04.000+09:00',
        'ancestry': None,
        'tag_type': 'category'},
        {'id': 168,
        'keyword': 'history',
        'name': '歴史',
        'desc': 'Readyforには歴史に関するプロジェクトがたくさんあります。  地域の歴史を掘り起こすプロジェクトや、歴史ある建造物、作品を修復するプロジェクトなど、様々な活動があります。 日本最大のクラウドファンディングReadyforには共感をテーマに、地域活性化に関するクリエイティブな活動や新しいことに挑戦する人々がたくさん集まっています。',
        'image_file_name': 'history.jpg',
        'image_content_type': 'image/jpeg',
        'image_file_size': 161091,
        'image_updated_at': '2017-05-10T16:30:41.000+09:00',
        'created_at': '2017-05-10T16:30:42.000+09:00',
        'updated_at': '2017-05-10T16:30:42.000+09:00',
        'ancestry': '113',
        'tag_type': 'normal'}],
        'lp_path': '/matching_gift',
        'degree': '6月30日',
        'expired_at_year': '2017年',
        'goal_amount': '20,000,000',
        'deadline': '2017-6-30',
        'news_update_count': 21,
        'comments_count': 465,
        'project_text': project_text,
        'project_images': ['https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/236526/content_c2ca448d931523f898d4b4a229dc0f3833b087fe.png" width="610', 'https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/233997/content_dcdfd41cb6e96e78736deb5f5add6f6311da8e80." width="610', 'https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/236535/content_45561166ea69349fd80b224b1dfbeaa50eb7ee2d.jpg" width="610', 'https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/237598/content_dcdfd41cb6e96e78736deb5f5add6f6311da8e80." width="610', 'https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/236618/content_dcdfd41cb6e96e78736deb5f5add6f6311da8e80." width="610', 'https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/237646/content_c2ca448d931523f898d4b4a229dc0f3833b087fe.png" width="610', 'https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/237599/content_c2ca448d931523f898d4b4a229dc0f3833b087fe.png" width="610', 'https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/237647/content_c2ca448d931523f898d4b4a229dc0f3833b087fe.png" width="610', 'https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/236614/content_dcdfd41cb6e96e78736deb5f5add6f6311da8e80." width="610', 'https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/236615/content_dcdfd41cb6e96e78736deb5f5add6f6311da8e80." width="610', 'https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/236611/content_dcdfd41cb6e96e78736deb5f5add6f6311da8e80." width="610', 'https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/236622/content_c2ca448d931523f898d4b4a229dc0f3833b087fe.png" width="610', 'https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/236620/content_c2ca448d931523f898d4b4a229dc0f3833b087fe.png" width="610', 'https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/236621/content_c2ca448d931523f898d4b4a229dc0f3833b087fe.png" width="610', 'https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/237614/content_dcdfd41cb6e96e78736deb5f5add6f6311da8e80." width="610', 'https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/237613/content_dcdfd41cb6e96e78736deb5f5add6f6311da8e80." width="610', 'https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/237615/content_5d114bc8e3c1fb8b1af736cdd793c3b8952ec315.jpg" width="610', 'https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/237651/content_dcdfd41cb6e96e78736deb5f5add6f6311da8e80." width="610', 'https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/237611/content_b629b7dc02fe6f5723da7d5f3dd63eb28fb5f3e4.jpg" width="610', 'https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/237600/content_339f5868588cfc8fda4a1ec94ead8f737c5fcfc0." width="150', 'https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/237601/content_339f5868588cfc8fda4a1ec94ead8f737c5fcfc0." width="150', 'https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/237602/content_339f5868588cfc8fda4a1ec94ead8f737c5fcfc0." width="150', 'https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/237603/content_339f5868588cfc8fda4a1ec94ead8f737c5fcfc0." width="150', 'https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/237604/content_339f5868588cfc8fda4a1ec94ead8f737c5fcfc0." width="150', 'https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/237605/content_339f5868588cfc8fda4a1ec94ead8f737c5fcfc0." width="150', 'https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/237606/content_339f5868588cfc8fda4a1ec94ead8f737c5fcfc0." width="150', 'https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/237607/content_339f5868588cfc8fda4a1ec94ead8f737c5fcfc0." width="150', 'https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/237608/content_339f5868588cfc8fda4a1ec94ead8f737c5fcfc0." width="150', 'https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/237609/content_339f5868588cfc8fda4a1ec94ead8f737c5fcfc0." width="150', 'https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/237610/content_339f5868588cfc8fda4a1ec94ead8f737c5fcfc0." width="150', 'https://readyfor.jp/s3/readyfor-img/ckeditor_assets/pictures/274203/thumb_c6749bf1fd05837bb38a2d3c7ee5631cec5a9ffa.jpg" alt="Thumb c6749bf1fd05837bb38a2d3c7ee5631cec5a9ffa" width="120" height="120']
    }
}



facebook_likes_dict = {
    "share": {
        "comment_count": 0,
        "share_count": 2384
      },
      "og_object": {
        "id": "1157872341001510",
        "description": "エジプト考古学研究者人生をかけた、最後にして最大の挑戦へ！ピラミッド建造の目的解明を目指して。鍵を握る「太陽の船」の完全修復と復原を目指します。 - クラウドファンディング Readyfor",
        "title": "人生最後の挑戦！ピラミッドの謎解明の鍵を握る太陽の船復原へ！ - クラウドファンディング Readyfor (レディーフォー)",
        "type": "website",
        "updated_time": "2017-05-19T05:35:21+0000"
      },
      "id": "https://readyfor.jp/projects/solarboat/"
}

backers = {
    "backers": [
        {'backer_id': '292568', 'backed_at': "2017-05-29"},
        {'backer_id': '292579', 'backed_at': "2017-05-28"},
        {'backer_id': '224007', 'backed_at': "2017-05-28"},
        {'backer_id': '262240', 'backed_at': "2017-05-23"},
        {'backer_id': '257498', 'backed_at': "2017-05-28"},
        {'backer_id': '292556', 'backed_at': "2017-05-28"},
    ],
    "max_page": 1
}
