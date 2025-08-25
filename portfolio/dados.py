habilidades = {
    'habilidade1': {
        'nome': 'Programação com Python',
        'nivel': 'Avançado',
        'descricao': 'Desenvolvimento de aplicações, análise de dados, automação e scripts com Python.',
        'icone': 'fa-python'
    },
    'habilidade2': {
        'nome': 'Geoprocessamento',
        'nivel': 'Especialista',
        'descricao': 'Análise espacial, processamento de dados geográficos e criação de mapas utilizando ferramentas GIS.',
        'icone': 'fa-map-marked-alt'
    },
    'habilidade3': {
        'nome': 'Dam Break',
        'nivel': 'Especialista',
        'descricao': 'Modelagem e análise de ruptura de barragens, estudos de propagação de ondas e avaliação de riscos.',
        'icone': 'fa-water'
    },
    'habilidade4': {
        'nome': 'Machine Learning',
        'nivel': 'Intermediário',
        'descricao': 'Implementação de algoritmos de aprendizado de máquina para análise de dados e previsões.',
        'icone': 'fa-brain'
    },
    'habilidade5': {
        'nome': 'Modelagem 3D e Simulação',
        'nivel': 'Avançado',
        'descricao': 'Criação de modelos tridimensionais e simulações para projetos de engenharia e visualização.',
        'icone': 'fa-cube'
    },
    'habilidade6': {
        'nome': 'Desenvolvimento Web',
        'nivel': 'Intermediário',
        'descricao': 'Criação de aplicações web utilizando Django, HTML, CSS e JavaScript.',
        'icone': 'fa-code'
    },
    'habilidade7': {
        'nome': 'Análise de Dados',
        'nivel': 'Avançado',
        'descricao': 'Processamento, visualização e interpretação de grandes conjuntos de dados para tomada de decisões.',
        'icone': 'fa-chart-bar'
    }
}


projetos = {
    'projeto1': {
        'titulo': 'Web Scraping Avançado',
        'descricao': 'Desenvolvimento de sistema automatizado para raspagem de dados e extração de informações de sites utilizando bibliotecas Python. O sistema coleta, processa e organiza dados de múltiplas fontes para análise posterior.',
        'tecnologias': 'Python, Pandas, HTML, Selenium, BeautifulSoup, Requests',
        'github': 'https://github.com/ReiJardim?tab=repositories',
        'data': '2024',
        'categoria': 'Análise de Dados',
        'destaque': True,
        'imagem': 'img/projeto_webscraping.png',
        'funcionalidades': [
            'Extração automatizada de dados de múltiplas fontes',
            'Processamento e limpeza de dados estruturados e não-estruturados',
            'Interface de usuário para configuração de parâmetros de coleta',
            'Exportação de dados em diversos formatos (CSV, JSON, Excel)'
        ]
    },
    'projeto2': {
        'titulo': 'Sistema Multi-Agentes para Escrita',
        'descricao': 'Desenvolvimento de um sistema multiagente para execução de atividades de escrita automatizada. A aplicação utiliza IA para coordenar diferentes agentes especializados que trabalham em conjunto para gerar conteúdo de alta qualidade.',
        'tecnologias': 'CREWAI, Python, NLP, APIs de IA, Langchain',
        'github': 'https://github.com/ReiJardim/test_multagentes',
        'data': '2024',
        'categoria': 'Inteligência Artificial',
        'destaque': True,
        'imagem': 'img/projeto_multiagentes.png',
        'funcionalidades': [
            'Criação de conteúdo técnico automatizado',
            'Capacidade de pesquisa e integração de informações',
            'Revisão e aprimoramento automático de textos',
            'Interface amigável para configuração e monitoramento dos agentes'
        ]
    },
    'projeto3': {
        'titulo': 'Plataforma GeoTech para Gerenciamento de Obras',
        'descricao': 'Desenvolvimento de plataforma web para otimização de serviços de geoprocessamento e gerenciamento de obras civis. O sistema integra funcionalidades de GIS com gerenciamento de projetos para acompanhamento completo do ciclo de vida de obras.',
        'tecnologias': 'Python, Streamlit, Pandas, GeoPandas, PostgreSQL/PostGIS, Plotly',
        'github': 'https://github.com/ReiJardim?tab=repositories',
        'data': '2023',
        'categoria': 'Geoprocessamento',
        'destaque': True,
        'imagem': 'img/projeto_geotech.png',
        'funcionalidades': [
            'Visualização de dados geoespaciais em tempo real',
            'Análise espacial avançada para planejamento de obras',
            'Monitoramento de cronogramas e recursos',
            'Geração de relatórios automáticos de progresso'
        ]
    },
    'projeto4': {
        'titulo': 'Sistema de Processamento de Áudio com IA',
        'descricao': 'Desenvolvimento de sistema para interação com áudios, implementando funcionalidades de transcrição, tradução e geração de áudio a partir de texto. A aplicação utiliza modelos avançados do Hugging Face para processamento de linguagem natural e áudio.',
        'tecnologias': 'Python, PyTorch, Transformers, SoundFile, Whisper, Librosa, FastAPI',
        'github': 'https://github.com/ReiJardim/huggingface_audio',
        'data': '2023',
        'categoria': 'Processamento de Áudio',
        'destaque': False,
        'imagem': 'img/projeto_audio.png',
        'funcionalidades': [
            'Transcrição de áudio em múltiplos idiomas',
            'Tradução automática de conteúdo de áudio',
            'Síntese de voz natural a partir de texto',
            'API RESTful para integração com outros sistemas'
        ]
    },
    'projeto5': {
        'titulo': 'Análise de Risco para Ruptura de Barragens',
        'descricao': 'Desenvolvimento de sistema para modelagem e análise de cenários de ruptura de barragens, incluindo simulações hidrodinâmicas, mapeamento de áreas de risco e planos de contingência.',
        'tecnologias': 'Python, HEC-RAS API, QGIS, ArcGIS, NumPy, Matplotlib',
        'github': 'https://github.com/ReiJardim?tab=repositories',
        'data': '2022',
        'categoria': 'Engenharia Civil',
        'destaque': True,
        'imagem': 'img/projeto_dambreak.png',
        'funcionalidades': [
            'Modelagem hidrodinâmica de propagação de ondas',
            'Mapeamento de áreas de inundação',
            'Cálculo de tempos de chegada e velocidades de fluxo',
            'Avaliação quantitativa de riscos a jusante'
        ]
    }
}

# Dados de experiências profissionais
experiencias = {
    'experiencia1': {
        'empresa': 'Empresa de Engenharia',
        'cargo': 'Engenheiro de Geoprocessamento',
        'periodo': '2023 - Presente',
        'descricao': 'Desenvolvimento de soluções de geoprocessamento para análise espacial e tomada de decisões em projetos de engenharia. Implementação de ferramentas automatizadas para processamento de dados geoespaciais utilizando Python e bibliotecas como GeoPandas e GDAL.',
        'atual': True
    },
    'experiencia2': {
        'empresa': 'Consultoria Ambiental',
        'cargo': 'Analista de Dam Break',
        'periodo': '2021 - 2023',
        'descricao': 'Realização de estudos de ruptura de barragens, análise de riscos e elaboração de planos de ação de emergência. Desenvolvimento de modelos hidrodinâmicos para simulação de cenários de ruptura utilizando HEC-RAS e ferramentas GIS.',
        'atual': False
    },
    'experiencia3': {
        'empresa': 'Startup de Tecnologia',
        'cargo': 'Desenvolvedor Python',
        'periodo': '2019 - 2021',
        'descricao': 'Desenvolvimento de aplicações e scripts para automação de processos e análise de dados utilizando Python e suas bibliotecas. Implementação de soluções de raspagem de dados e processamento de informações para clientes de diversos segmentos.',
        'atual': False
    }
}

# Dados de formação acadêmica
formacoes = {
    'formacao1': {
        'instituicao': 'Universidade Federal',
        'curso': 'Engenharia Civil',
        'grau': 'Bacharelado',
        'periodo': '2015 - 2020',
        'descricao': 'Especialização em Recursos Hídricos e Saneamento. Projeto de conclusão focado em modelagem hidrodinâmica para análise de ruptura de barragens.'
    },
    'formacao2': {
        'instituicao': 'Instituto Técnico',
        'curso': 'Especialização em Geoprocessamento',
        'grau': 'Pós-graduação',
        'periodo': '2021 - 2022',
        'descricao': 'Formação especializada em técnicas avançadas de geoprocessamento e análise de dados espaciais para aplicações em engenharia.'
    },
    'formacao3': {
        'instituicao': 'Plataforma Online de Educação',
        'curso': 'Data Science e Machine Learning',
        'grau': 'Certificação Profissional',
        'periodo': '2022',
        'descricao': 'Formação intensiva em ciência de dados, aprendizado de máquina e visualização de dados utilizando Python, Pandas, Scikit-learn e TensorFlow.'
    }
}
