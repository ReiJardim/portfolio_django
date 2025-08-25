from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    icone = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nome']

class Habilidade(models.Model):
    NIVEL_CHOICES = [
        ('Básico', 'Básico'),
        ('Intermediário', 'Intermediário'),
        ('Avançado', 'Avançado'),
        ('Especialista', 'Especialista')
    ]
    
    nome = models.CharField(max_length=100)
    nivel = models.CharField(max_length=20, choices=NIVEL_CHOICES, default='Intermediário')
    descricao = models.TextField(blank=True, null=True)
    icone = models.CharField(max_length=50, blank=True, null=True)
    ordem = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.nome} - {self.nivel}"
    
    class Meta:
        verbose_name = 'Habilidade'
        verbose_name_plural = 'Habilidades'
        ordering = ['ordem', 'nome']

class Projeto(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    descricao = models.TextField()
    tecnologias = models.CharField(max_length=255)
    data_criacao = models.DateField()
    github = models.URLField(blank=True, null=True)
    site_projeto = models.URLField(blank=True, null=True)
    imagem = models.ImageField(upload_to='projetos/', blank=True, null=True)
    destaque = models.BooleanField(default=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'
        ordering = ['-data_criacao']

class ProjetoDetalhe(models.Model):
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='detalhes')
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    ordem = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.projeto.titulo} - {self.titulo}"
    
    class Meta:
        verbose_name = 'Detalhe do Projeto'
        verbose_name_plural = 'Detalhes dos Projetos'
        ordering = ['ordem']

class Formacao(models.Model):
    instituicao = models.CharField(max_length=200)
    curso = models.CharField(max_length=200)
    grau = models.CharField(max_length=100)
    periodo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    logo = models.ImageField(upload_to='formacao/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.curso} - {self.instituicao}"
    
    class Meta:
        verbose_name = 'Formação'
        verbose_name_plural = 'Formações'
        ordering = ['-periodo']

class Experiencia(models.Model):
    empresa = models.CharField(max_length=200)
    cargo = models.CharField(max_length=200)
    periodo = models.CharField(max_length=100)
    descricao = models.TextField()
    logo = models.ImageField(upload_to='experiencia/', blank=True, null=True)
    atual = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.cargo} - {self.empresa}"
    
    class Meta:
        verbose_name = 'Experiência'
        verbose_name_plural = 'Experiências'
        ordering = ['-atual', '-periodo']

class Certificacao(models.Model):
    nome = models.CharField(max_length=200)
    emissor = models.CharField(max_length=200)
    data_emissao = models.DateField()
    descricao = models.TextField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.nome} - {self.emissor}"
    
    class Meta:
        verbose_name = 'Certificação'
        verbose_name_plural = 'Certificações'
        ordering = ['-data_emissao']

class Contato(models.Model):
    tipo = models.CharField(max_length=100)
    valor = models.CharField(max_length=255)
    icone = models.CharField(max_length=50, blank=True, null=True)
    ordem = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.tipo}: {self.valor}"
    
    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'
        ordering = ['ordem']
