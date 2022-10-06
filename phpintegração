<?php

    function verificaropcaomenu($opcao){
        switch($opcao){
            case 1:
                echo "=== Menu Cadastro ===" . PHP_EOL;
                break;
            case 2:
                echo "=== Lista Aluno ===" . PHP_EOL;
                break;
            case 3:
                echo "=== Menu Excluir ===" . PHP_EOL;
                break;
            case 4:
                echo "=== Menu Alterar ===" . PHP_EOL;
                break;
        }

    //    if($opcao == 1){
    //        echo "=== Menu Cadastro ===" . PHP_EOL;
    //        echo('');
    //    }
    //    else if($opcao == 2){
    //        echo "=== Lista Alunos ===" . PHP_EOL;
    //        echo('');
    //    }
    //    else if($opcao == 3){
    //        echo "=== Menu Excluir ===" . PHP_EOL;
    //        echo('');
    //    }
    //    else if($opcao == 4){
    //        echo "=== Menu Alterar ===" . PHP_EOL;
    //        echo('');
    //    }

    }


    $listaOpcoesValidas = [1,2,3,4,5];
    
    $opcao = 0;

    while($opcao != 5) {

    echo "====== Menu ======" . PHP_EOL;
    echo "1 - Cadastrar Aluno" . PHP_EOL;
    echo "2 - Listar os alunos" . PHP_EOL;
    echo "3 - Excluir aluno" . PHP_EOL;
    echo "4 - Atualizar dados do aluno" . PHP_EOL;
    echo "5 - Sair" . PHP_EOL;

    
    $opcao = readline('Digite a opção que você deseja: ');

    #if($opcao != 1 && $opcao != 2 && $opcao != 3 && $opcao != 4 && $opcao != 5)

    if(!in_array($opcao,$listaOpcoesValidas)){
        echo('');
        echo('-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-') . PHP_EOL;
        echo("!!!!! OPÇÃO INVALIDA !!!!!") . PHP_EOL;
        echo('-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-') . PHP_EOL;
        echo('');
        }
        verificaropcaomenu($opcao);
    }

?>
