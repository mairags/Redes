# Redes
Terceiro credito da disciplina Redes de Computadores 1

Alunos: Maira Gomes Santos e Joao Henrique dos Santos Queiroz

Descrição:

Uma rede de computadores caracteriza-se por dois ou mais computadores interligados, não importando por qual meio (cabos, ondas de rádio etc), desde que sejam capazes de trocar informações entre si e/ou compartilhar seus recursos de hardware. Uma rede funciona sob protocolos (que são regras que definem o funcionamento dela) e a família de protocolos mais conhecida e utilizada é a TCP/IP, que engloba os protocolos IP (da camada de rede), TCP e UDP (da camada de transporte), HTTP (da camada de aplicação) entre outros.

Cliente: 

O programa cliente primeiro cria um socket  através da função socket(). Em seguida ele se conecta ao servidor através da função connect() e inicia um loop (laço) que fica fazendo send() (envio) e recv() (recebimento) com as mensagens específicas da aplicação. É no par send, recv que temos a comunicação lógica. Quando alguma mensagem da aplicação diz que é o momento de terminar a conexão, o programa chama a função close() para finalizar o socket.

Servidor: 

O programa servidor também utiliza a mesma API de sockets. Ou seja, inicialmente ele também cria um socket. No entanto, diferentemente do cliente, o servidor precisa fazer um bind(), que associa o socket a uma porta do sistema operacional, e depois utilizar o listen() para escutar novas conexões de clientes nessa porta.

Quando um novo cliente faz uma nova conexão, a chamada accept() é utilizada para começar a se comunicar. Da mesma forma que no cliente, o servidor fica em um loop (laço) recebendo e enviando mensagens através do par de funções send()  e recv(). Quando a comunicação com o cliente termina, o servidor volta a aguardar novas conexões de clientes.

Principais funções para escrever programas com sockets:
 
socket()       // Cria um socket e retorna o descritor de arquivo
bind()         // Associa o socket a um endereço socket e uma porta
connect()      // Tenta estabelecer uma conexão com um socket
listen()       // Coloca o socket para aguardar conexões
accept()       // Aceita uma nova conexão e cria um socket
send()         // caso conectado, transmite mensagens ao socket
recv()         // recebe as mensagens através do socket 
close()        // desaloca o descritor de arquivo



Criar objeto socket 

Criamos um objeto do tipo socket usando o método socket(), o qual recebe dois ou três parâmetros.

Família de endereços
AF_INET(endereço IPv4)
Tipo de socket
SOCK_STREAM (para socket TCP)

Interfaces de sockets 
A interface de um socket se diferencia pelos diferentes serviços que são fornecidos 

Interface de sockets de fluxo(stream). Define um serviço orientado a conexão confiável (TCP). Dados são enviados sem erros ou duplicação e recebidos na mesma ordem em que foram enviados. SOCK_STREAM

Neste trabalho o protocolo de transporte usado foi TCP pois é mais confiável e garante a entrega das informações. O protocolo TCP possui algumas vantagens. Os sockets do tipo TCP são orientados a conexão e tem um canal exclusivo de comunicação entre cliente e servidor. Eles garantem a ordem dos pacotes, são considerados confiáveis e sem perda. No entanto, quando se trata de se recuperar de falhas e perda de pacotes ele é mais burocrático e lento.

