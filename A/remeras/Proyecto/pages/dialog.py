import reflex as rx

def dialog(nombre,title,icono):
    return rx.dialog.root(
                rx.dialog.trigger(
                    rx.button(
                        title,
                        rx.icon(icono, size=20),
                          color='white',
                          variant='ghost',
                          radius='none',
                          size='2',

                    )
                ),
                rx.dialog.content(
                    nombre(),
                    background_color='rgba(0,0,0,0.75)',
                    max_width='90vw',
                    width='auto',
                ),
         
     ),


# rx.dialog.root(
#     rx.dialog.trigger(rx.button("Open Dialog")),
#     rx.dialog.content(
#         rx.dialog.title("Welcome to Reflex!"),
#         rx.dialog.description(
#             "This is a dialog component. You can render anything you want in here.",
#         ),
#         rx.dialog.close(
#             rx.button("Close Dialog", size="3"),
#         ),
#         max_width="100vw", # Make this a bigger value, it's fixed by default.
#         width="100vw",
#     ),
# )

# rx.dialog.root(
#     rx.dialog.trigger(rx.button("Edit Profile", size="4")),
#     rx.dialog.content(
#         rx.dialog.title("Edit Profile"),
#         rx.dialog.description(
#             "Change your profile details and preferences.",
#             size="2",
#             margin_bottom="16px",
#         ),
#         rx.flex(
#             rx.dialog.close(
#                 rx.button(
#                     "Cancel",
#                     color_scheme="gray",
#                     variant="soft",
#                 ),
#             ),
#             rx.dialog.close(
#                 rx.button("Save"),
#             ),
#             spacing="3",
#             margin_top="16px",
#             justify="end",
#         ),
#     ),
# )