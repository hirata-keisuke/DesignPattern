---

theme: "Solarized"
title: "Factory Method"
slideNumber: true

---
<style type="text/css"> p,li { font-size:0.8em; text-align:left; }
</style>

## Factory Methodパターン
<table style="border:none;">
    <tr style="border:none;">
        <td style="border:none;"><img src="./Images/いらすとや/釘.png" alt="釘" style="height:1cm;"></td>
        <td style="border:none;"><img src="./Images/いらすとや/右矢印.png" alt="右矢印" style="height:1cm;"></td>
        <td style="border:none;"><img src="./Images/いらすとや/工場.png" alt="工場" style="height:4cm;"></td>
        <td style="border:none;"><img src="./Images/いらすとや/左矢印.png" alt="左矢印" style="height:1cm;"></td>
        <td style="border:none;"><img src="./Images/いらすとや/木材.png" alt="木材" style="height:1cm;"></td>
    </tr>
    <tr style="border:none;">
        <td style="border:none;"></td>
        <td style="border:none;"></td>
        <td style="border:none;"><img src="./Images/いらすとや/下矢印.png" alt="下矢印" style="height:3cm;"></td>
        <td style="border:none;"></td>
        <td style="border:none;"></td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td><img src="./Images/いらすとや/法隆寺.png" alt="法隆寺" style="height:4cm;"></td>
        <td></td>
        <td></td>
    </tr>
</table>

---

## 目的

オブジェクトを生成するときのインタフェースだけを規定して、実際にどのクラスをインスタンス化するかはサブクラスが決めるようにする。Factory Methodパターンは、インスタンスかサブクラスに任せる。

<img src="./Images/FactoryMethod.png" alt="class_diagram" style="border:none; box-shadow:none; width:20cm;">

---

## こんな時に使えるかも

- クラスが生成しなければならないオブジェクトのクラスを事前に知ることができない場合

- サブクラス化により、生成するオブジェクトを特定化する場合

- クラスが責任をいくつかのサブクラスの中の一つに移譲するときに、どのサブクラスに移譲するかを局所化したい場合

---

## 結果

1. サブクラスに手がかりを提供する<br>
Creatorクラスのfactory methodが、Creatorのサブクラスでのオーバーライドの内容のヒントになりうる。

2. パラレルなクラス階層をつなぐ<br>
Creatorクラスのfactory methodがProductクラスのインスタンスを返すようにしつつ、CreatorのサブクラスではProductのサブクラスを返すように実装すれば型が合う。

3. ユーザ定義のConcreteProductと協調させられる<br>
アプリケーションはProductのインタフェースしか扱わないので、ユーザ定義のProductのサブクラスでも使える。

4. サブクラスのために実装しなくてはならない<br>
ConcreteProductを生成するために、そのためのfactory methodを実装したCreatorのサブクラスを作らなくてはならない。

---

## 実装のヒント

- Creatorを抽象クラスとして、そのfactory methodの実装をサブクラスに全て任せる場合<br>
振る舞いを予測できないクラスをインスタンス化しなければならないジレンマを回避する。

- Creatorを具象クラスとして、そのfactory methodの実装を一応与えておく場合<br>
オブジェクトの生成は、サブクラスでその生成方法をオーバライドできるように、1つのメソッドにまとめておく。

- factory methodがパラメータを受け取って、生成するオブジェクトを識別するようにできる