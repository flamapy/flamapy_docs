FROM ruby:latest

ENV LC_ALL C.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8

WORKDIR /usr/src/app

# Instalar dependencias de compilación para nokogiri, protobuf, etc.
RUN apt-get update -qq && \
    apt-get install -y build-essential libxml2-dev libxslt1-dev && \
    rm -rf /var/lib/apt/lists/*

# Evitar warning de git
RUN git config --global --add safe.directory /usr/src/app

# Copiar gemspec y Gemfile
COPY Gemfile Gemfile.lock just-the-docs.gemspec ./

# Instalar bundler y las gems en /usr/local/bundle (volumen recomendado)
RUN gem install bundler && bundle install

EXPOSE 4000

CMD ["bundle", "exec", "jekyll", "serve", "--host", "0.0.0.0"]
