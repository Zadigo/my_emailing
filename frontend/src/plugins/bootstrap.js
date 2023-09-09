import { h, ref, withModifiers, isRef, watch, onMounted, unref, onBeforeUnmount } from 'vue'
import { RouterLink } from 'vue-router'

import 'bootstrap/dist/css/bootstrap.min.css'
import 'mdb-ui-kit/css/mdb.min.css'
import '../assets/vuebootstrap.css'

{/* <div class="btn-group">
    <button type="button" class="btn btn-primary">Reference</button>
    <button
        type="button"
        class="btn btn-primary dropdown-toggle dropdown-toggle-split"
        id="dropdownMenuReference"
        data-mdb-toggle="dropdown"
        aria-expanded="false"
        data-mdb-reference="parent"
    >
        <span class="visually-hidden">Toggle Dropdown</span>
    </button>
    <ul class="dropdown-menu" aria-labelledby="dropdownMenuReference">
        <li><a class="dropdown-item" href="#">Action</a></li>
        <li><a class="dropdown-item" href="#">Another action</a></li>
        <li><a class="dropdown-item" href="#">Something else here</a></li>
        <li><hr class="dropdown-divider" /></li>
        <li><a class="dropdown-item" href="#">Separated link</a></li>
    </ul>
</div> */}

// const useDarkmode = function() {
//     const darkMode = ref(false)
//     return {
//         darkMode
//     }
// }

// const useMedia = function (query) {
//     const mediaQuery = window.matchMedia(query)
//     const matches = ref(mediaQuery.matches)
//     useEventListener(mediaQuery, 'change', (e) => {
//         matches.value = event.matches
//     })
//     return matches;
// }
// useMedia('(prefers-color-scheme: dark)')
// useMedia('(prefers-color-scheme: light)')
// const isTablet = useMedia('(min-width: 640px)');

function useEventListener (target, event, handler) {
    if (isRef(target)) {
        watch(target, (value, oldValue) => {
            oldValue?.removeEventListener(event, handler)
            value?.addEventListener(event, handler)
        })
    } else {
        onMounted(() => {
            target.addEventListener(event, handler)
        })
    }

    onBeforeUnmount(() => {
        unref(target)?.removeEventListener(event, handler);
    })
}
 
function useOnClickOutside (rootEl, callback) {
    console.log(rootEl)
    // `mousedown` or `mouseup` is better than `click` here because it doesn't bubble up like `click`
    // if you've used `click` here, the callback will be run immediatly.
    useEventListener(window, 'mouseup', (e) => {
        const clickedEl = e.target
        // skip if the root element contains the clicked element
        if (rootEl.value?.contains(clickedEl)) {
            return
        }
        // otherwise execute the action
        callback()
    })
}

function useDropdown () {
    const items = ref([])
    const show = ref(false)
    function toggleDropdown () {
        show.value = ! show.value
        // el.style.position = 'absolute'
    }
    return {
        items,
        show,
        toggleDropdown
    }
}


/**
 * Bootstrap button
 */
const BButton = {
    name: 'BButton',
    emits: ['click'],
    props: {
        color: {
            type: String,
            default: 'primary'
        },
        to: {
            type: String
        }
    },
    computed: {
        buttonClasses () {
            return [
                'btn',
                {
                    [`btn-${this.color}`]: true
                }
            ]
        },
    },
    render (vm) {
        return h(this.to ? RouterLink : 'button', {
            type: 'button',
            class: this.buttonClasses,
            to: this.to,
            onClick: () => {
                this.$emit('click')
            }
        }, [
            vm.$slots.default()
        ])
    }
}

const BSplitDropButton = {
    name: 'BSplitDropButton',
    props: {
        buttonName: {
            type: String
        },
        color: {
            type: String,
            default: 'primary'
        },
        transition: {
            type: String,
            default: 'scale'
        },
        items: {
            type: Array
        }
    },
    setup () {
        const { show, toggleDropdown } = useDropdown()
        var buttonRef = null
        useOnClickOutside(buttonRef, toggleDropdown)
        return {
            buttonRef,
            show,
            toggleDropdown
        }
    },
    watch: {
        show (current) {
            if (current) {
                this.$refs.link.style.position = 'absolute'
                this.$refs.link.style.top = '38px'
                // this.$refs.link.style.inset = '0px auto auto 0px'
                // this.$refs.link.style.margin = '0px'
                // this.$refs.link.style.transform = 'translate(0px, 38px)'
            } else {
                this.$refs.link.style = null 
            }
        }
    },
    computed: {
        dropdownClasses () {
            return [
                'dropdown-menu',
                this.show ? 'show' : null,
                this.transition
            ]
        }
    },
    methods: {
        getLink (item) {
            // if (item.to) {
            //     return h(RouterLink, {
            //         to: item.to
            //     })
            // }

            // if (item.href) {
            //     return h('a', {
            //         class: 'dropdown-item',
            //         href: item.href,
            //         // onClick: withModifiers(linkClick, ['prevent'])
            //     },
            //     [
            //         item.name
            //     ])
            // }
            return h('a', {
                class: 'dropdown-item',
                href: item.href,
                // onClick: withModifiers(linkClick, ['prevent'])
            },
            [
                item.name
            ])
        },
        getDropdown () {
            return h('ul', {
                'aria-lalledby': 'something',
                ref: 'link',
                class: this.dropdownClasses
            }, [
                this.items.map((item) => {
                    return h('li', {}, [
                        this.getLink(item)
                    ])
                })
            ])
            // return h('ul', {
            //         'aria-labelledby': 'dropdownMenuButton',
            //         ref: 'link'
            //     }, [
            //         this.items.value.map((item) => {
            //             return h('li', {}, [
            //                 this.getLink(item)
            //             ])
            //     })
            // ])
        }
    },
    render () {
        return h('div', {
            class: 'btn-group',
            // 'aria-expanded': this.show
        }, [
            h(BButton, {
                color: this.color
            }, () => this.buttonName),
            h(BButton, {
                color: this.color,
                ref: this.buttonRef,
                class: [
                    'dropdown-toggle dropdown-toggle-split',
                    {
                        show: this.show
                    }
                ],
                onClick: this.toggleDropdown
            }, () => [
                <span class="visually-hidden">Toggle Dropdown</span>
            ]),
            this.getDropdown()
        ])
    }
}

/**
 * Bootstrap dropdown button
 *
 */ 
const BDropdownButton = {
    name: 'BDropdownButton',
    emits: ['dropdown-expanded'],
    props: {
        id: {
            type: String,
            required: true
        },
        transition: {
            type: String,
            default: 'scale'
        },
        items: {
            type: Array,
            default: () => [
                {
                    name: 'Google 1',
                    href: '#',
                    to: '#'
                },
                {
                    name: 'Google 2',
                    href: '#',
                    to: '#'
                }
            ]
        },
        buttonName: {
            type: String
        },
        color: {
            type: String,
            default: 'primary'
        }
    },
    data: () => ({
        show: false
    }),
    computed: {
        buttonClasses () {
            return [
                'btn dropdown-toggle',
                {
                    [`btn-${this.color}`]: true
                },
                this.show ? 'show' : null
            ]
        },
        dropdownClasses () {
            return [
                'dropdown-menu',
                this.show ? 'show': null,
                this.transition
            ]
        }
    },
    mounted () {
        var body = document.querySelector('body')
        body.addEventListener('click', this.windowListener)
    },
    unmounted () {
        var body = document.querySelector('body')
        body.removeEventListener('click', this.windowListener)
    },
    methods: {
        expandDropdown () {
            this.show = !this.show
            this.$emit('dropdown-expanded', this.show)
        },
        windowListener (e) {
            console.log(e)
        },
        getLink (item) {
            if (item.href) {
                return h('a', {
                    class: 'dropdown-item',
                    href: item.href,
                    onClick: withModifiers(this.linkClick, ['prevent'])
                },
                [
                    item.name
                ])
            }

            if (item.to) {
                return h(RouterLink, {
                    to: item.to
                })
            }
        },
        linkClick (index) {
            this.$emit('dropdown-click', index)
        }
    },
    render () {
        return h('div', {
            class: 'dropdown',
        }, [
            h('button', {
                id: this.id,
                type: 'button',
                class: this.buttonClasses,
                onClick: this.expandDropdown
            }, [
                this.buttonName
            ]),
            
            h('ul', {
                'aria-labelledby': 'dropdownMenuButton',
                ref: 'link',
                class: this.dropdownClasses
            }, [
                this.items.map((item) => {
                    return h('li', {}, [
                        this.getLink(item)
                    ])
                })
            ])
            // h(Transition, { name: 'opacity' }, {
            //     default: () => this.show ? h('ul', {
            //         'aria-labelledby': 'dropdownMenuButton',
            //         class: this.dropdownClasses
            //     }, [
            //         this.items.map((item) => {
            //             return h('li', {}, [
            //                 this.getLink(item)
            //             ])
            //         })
            //     ]) : null
            // })
        ])
    }
}

export {
    BButton,
    BDropdownButton,
    BSplitDropButton,
    useEventListener,
    useOnClickOutside
}
