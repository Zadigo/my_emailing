export function createScript (src, useAsync = false) {
  const script = document.createElement('script')
  const url  = document.createAttribute('src')
  url.value = src
  script.setAttributeNode(url)

  if (useAsync) {
    const attribute = document.createAttribute('async')
    script.setAttributeNode(attribute)
  }

  return script
}
