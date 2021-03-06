SKELETON = """  version: '3'
  services:
   db:
     image: postgres:9.6.6
     container_name: dva-pg
     volumes:
      - dvapgdata:/var/lib/postgresql/data
     env_file:
       - ../../../custom.env
   rabbit:
     image: rabbitmq
     container_name: dva-rmq
     env_file:
       - ../../../custom.env
     volumes:
       - dvarabbit:/var/lib/rabbitmq
   redis:
     image: bitnami/redis:latest
     container_name: dva-redis
     env_file:
       - ../../../custom.env
     volumes:
       - dvaredis:/bitnami       
   webserver:
     image: akshayubhat/dva-auto:gpu
     container_name: webserver
     env_file:
       - ../../../custom.env
     environment:
       - LAUNCH_SERVER_NGINX=1       
     command: bash -c "git reset --hard && git pull && sleep 10 && ./start_container.py"
     ports:
       - "127.0.0.1:8000:80"
       - "127.0.0.1:8888:8888"
     depends_on:
       - db
       - redis       
       - rabbit
     volumes:
       - dvadata:/root/media
   non-gpu-workers:
     image: akshayubhat/dva-auto:gpu
     env_file:
       - ../../../custom.env
     environment:
       - LAUNCH_BY_NAME_retriever_inception=1
       - LAUNCH_BY_NAME_retriever_facenet=1
       - LAUNCH_Q_qextract=1
       - LAUNCH_Q_qstreamer=1
       - LAUNCH_SCHEDULER=1
       - LAUNCH_Q_GLOBAL_RETRIEVER=1
     command: bash -c "git reset --hard && git pull && sleep 45 && ./start_container.py"
     depends_on:
       - db
       - redis       
       - rabbit
     volumes:
       - dvadata:/root/media
{gpu_workers}
   global-model:
     image: akshayubhat/dva-auto:gpu
     env_file:
       - ../../../custom.env
     environment:
       - GPU_AVAILABLE=1     
       - NVIDIA_VISIBLE_DEVICES={global_model_gpu_id}
       - GPU_MEMORY={global_model_memory_fraction}
       - LAUNCH_Q_GLOBAL_MODEL=1
     command: bash -c "git reset --hard && git pull && sleep 45 && ./start_container.py"
     depends_on:
       - db
       - redis       
       - rabbit
     volumes:
       - dvadata:/root/media
  volumes:
   dvapgdata:
   dvadata:
   dvarabbit:
   dvaredis:
    """


BLOCK = """   {worker_name}:
         image: akshayubhat/dva-auto:gpu
         env_file:
           - ../../../custom.env
         environment:
           - GPU_AVAILABLE=1
           - NVIDIA_VISIBLE_DEVICES={gpu_id}
           - GPU_MEMORY={memory_fraction}
           - {env_key}={env_value}
         command: bash -c "git reset --hard && git pull && sleep 45 && ./start_container.py"
         depends_on:
           - db
           - redis       
           - rabbit
         volumes:
           - dvadata:/root/media"""


CPU_BLOCK = """   {worker_name}:
         image: akshayubhat/dva-auto:latest
         env_file:
           - ../../../custom.env
         environment:
           - {env_key}={env_value}
         command: bash -c "git reset --hard && git pull && sleep 45 && ./start_container.py"
         depends_on:
           - db
           - redis       
           - rabbit
         volumes:
           - dvadata:/root/media"""
