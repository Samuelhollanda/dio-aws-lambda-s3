import json
import urllib.parse

def lambda_handler(event, context):
    try:
        # Extraindo os dados do primeiro (e geralmente único) registro do evento
        record = event['Records'][0]
        
        # Pegando o nome do bucket e do arquivo
        bucket_name = record['s3']['bucket']['name']
        file_name = urllib.parse.unquote_plus(record['s3']['object']['key'], encoding='utf-8')
        
        # O print no Python envia os dados direto para o CloudWatch Logs
        print("🚀 Novo evento do S3 detectado!")
        print(f"📁 Bucket de origem: {bucket_name}")
        print(f"📄 Arquivo recebido: {file_name}")
        
        return {
            'statusCode': 200,
            'body': json.dumps(f'Sucesso! O arquivo {file_name} foi processado.')
        }
    except Exception as e:
        print(f"❌ Erro ao processar o evento: {e}")
        raise e