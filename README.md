# FoodHouse
FoodHouse es un blog de recetas de comida, donde podés registrarte para ver las recetas que otros usuarios compartieron y crear las tuyas

La página cuenta con diferentes pantallas:
* Landing Page
* Registro
* Login
* Blog

## Landing Page
Es donde nuestros usuarios ingresan por primera vez. El objetivo es comentarles un poco acerca del sitio y convencerlos para que se creen una cuenta.
![image](https://github.com/CiroJSCH/FoodHouse/assets/104742538/0c138d0e-ba92-4e80-bf6e-43b0b3844d27)
Aquí podemos navegar al blog y a la parte de About, donde se da más información acerca del sitio.

## Registro
Si el usuario quiere acceder al blog, debe tener una cuenta. Para eso, tiene que completar el formulario que se muestra en la imagen de abajo, donde se nos pide un email, un nombre de usuario y contraseña. Si ingresamos un mail inválido, dejamos campos vacíos o las contraseñas no coinciden, obtendremos un error y no podremos registrarnos.
![image](https://github.com/CiroJSCH/FoodHouse/assets/104742538/877fc5f8-020d-43c8-8269-faa2fcaf4cf4)

## Login
Cuando ya tenemos la cuenta creada, tenemos que iniciar sesión. Se nos pide el mail y la contraseña que, en caso de ser incorrecta, nos lanzará un error.
![image](https://github.com/CiroJSCH/FoodHouse/assets/104742538/4cebf9af-606a-471d-b9c1-9dbbe91a7e62)

## Blog
Es la parte más grande y con mayor funcionalidad del proyecto. Contamos con varias funcionalidades, detalladas brevemente a continuación:

### Página principal
Es donde van a aparecer listadas todas las recetas creadas. Contamos con un panel de filtros por comida y duración. En la parte superior hay una barra de búsqueda, una opción para acceder a nuestras recetas favoritas, sistema de chat y nuestro perfil.

Podemos aplicar una búsqueda por nombre de la receta, y obtendremos todas las recetas que coincidan o incluyan el término ingresado. En caso de no haber resultados, se nos notificará.

![image](https://github.com/CiroJSCH/FoodHouse/assets/104742538/54f37167-eac6-4af5-85c8-a38f92a71f49)

### Página de favoritos
Podemos agregar recetas a favoritos y acceder a ellas más facilmente en la página de favoritos.

![image](https://github.com/CiroJSCH/FoodHouse/assets/104742538/209ca1b0-21f5-4be1-a258-414d28a8931a)

### Página de detalle de receta
Si quiero acceder a una receta en particular, voy a poder ver su detalle, que incluye título, duración, dificultad, cantidad de likes, ingredientes, autor, cuando podemos cocinar esa receta y una descripción.
![image](https://github.com/CiroJSCH/FoodHouse/assets/104742538/0319c23e-5253-4c83-80f2-3c35e413741b)

Desde aquí puedo realizar acciones como:
- Darle Like
- Añadirla a favoritos
- Ir al perfil del creador
- Editarla y eliminarla (si soy el autor)

### Perfil
Puedo acceder a mi perfil o al de otro usuario y ver las recetas creadas, junto con su información y algunos datos extra. Si estoy en mi perfil, voy a poder editarlo. Si estoy en el perfil de otro usuario, voy a tener la opción de enviarle un mensaje.
![image](https://github.com/CiroJSCH/FoodHouse/assets/104742538/0d4d47ac-1fe7-48d9-87d9-b53050c6923c)

### Editar perfil
Vamos a poder completar nuestro perfil con nuestra foto de perfil, nombre y una descripción. Esta opción también la tenemos inmediatamente luego de registrarnos en el sitio.
![image](https://github.com/CiroJSCH/FoodHouse/assets/104742538/0150c4e2-23dc-4dda-8151-2b4302eb5310)


### Crear / Editar receta
Podemos crear nuestra propia receta, así como también editarla. Cuando guardamos el formulario, se aplican validaciones y la receta se guarda como la más reciente en la página principal y también en nuestro perfil en la parte de mis recetas.
![image](https://github.com/CiroJSCH/FoodHouse/assets/104742538/a407409d-3f63-47c8-ac68-28a02ac2ab73)

### Sistema de chat
La aplicación cuenta con un sistema de chat. Podemos enviar mensajes a otros usuarios.
![image](https://github.com/CiroJSCH/FoodHouse/assets/104742538/b3f96fa6-469e-46da-9557-968ff48ecb64)


## Tecnologías usadas
Para el desarrollo, se utilizó:
- Django
- Django REST Framework
- JavaScript
- TailwindCSS
- SQLite3

## Enlace al proyecto
En el siguiente video, se muestras las funcionalidades del sitio en mayor detalle.

[Video de presentación de FoodHouse](https://drive.google.com/file/d/1ktc0i1pPYWHrW5HgEhQ3z2UEc2DLkXi1/view?usp=sharing)
